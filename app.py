import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from typing import List, Dict, Any
import time
from config import SUBJECTS, APP_CONFIG, API_CONFIG, UI_MESSAGES, SYSTEM_PROMPT_TEMPLATE
from utils import (
    format_timestamp, truncate_text, export_chat_history, 
    validate_question, display_chat_statistics, safe_get_subject_info
)
from styles import apply_custom_styling

# Try to import PDF processing libraries
try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

class EducationalTutor:
    def __init__(self):
        # Configure the model with additional parameters for Gemini 2.0 Flash
        generation_config = {
            "temperature": API_CONFIG.get("temperature", 0.7),
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": API_CONFIG.get("max_tokens", 8192),
        }
        
        # Try to use Gemini 2.0 Flash, fall back to stable model if not available
        try:
            self.model = genai.GenerativeModel(
                model_name=API_CONFIG["model_name"],
                generation_config=generation_config
            )
            self.model_name = API_CONFIG["model_name"]
        except Exception as e:
            # Fallback to stable Gemini model
            fallback_model = "gemini-pro"
            st.warning(f"⚠️ Gemini 2.0 Flash not available, using {fallback_model} instead. Error: {str(e)}")
            self.model = genai.GenerativeModel(
                model_name=fallback_model,
                generation_config=generation_config
            )
            self.model_name = fallback_model
            
        self.subjects = SUBJECTS
    
    def create_system_prompt(self, subject: str, chat_history: List[Dict], reference_content: str = "") -> str:
        """Create a structured prompt for the Gemini API"""
        # Get subject context from both default and custom subjects
        all_subjects = get_all_subjects()
        subject_context = all_subjects.get(subject, {}).get("context", subject)
        
        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
            subject=subject,
            subject_context=subject_context
        )
        
        # Add reference content if available
        if reference_content and reference_content.strip():
            system_prompt += f"\n\nReference Material:\nThe user has provided the following reference material to help answer questions:\n\n{reference_content[:2000]}{'...' if len(reference_content) > 2000 else ''}\n\nPlease use this reference material when relevant to answer questions."
        
        # Add chat history for context
        if chat_history:
            system_prompt += "\n\nPrevious conversation context:\n"
            max_history = API_CONFIG["max_chat_history"]
            for i, exchange in enumerate(chat_history[-max_history:]):
                system_prompt += f"Q{i+1}: {exchange['question']}\n"
                system_prompt += f"A{i+1}: {exchange['answer'][:200]}...\n\n"
        
        return system_prompt
    
    def get_response(self, question: str, subject: str, chat_history: List[Dict], reference_content: str = "") -> str:
        """Get response from Gemini API"""
        try:
            system_prompt = self.create_system_prompt(subject, chat_history, reference_content)
            full_prompt = f"{system_prompt}\n\nCurrent question: {question}\n\nPlease provide a comprehensive answer:"
            
            response = self.model.generate_content(full_prompt)
            return response.text
        
        except Exception as e:
            error_str = str(e).lower()
            if "quota" in error_str or "limit" in error_str:
                return UI_MESSAGES["quota_exceeded"]
            elif "timeout" in error_str:
                return UI_MESSAGES["timeout_error"]
            else:
                return f"{UI_MESSAGES['general_error']}\n\nError details: {str(e)}"

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    if not PDF_AVAILABLE:
        return "PDF processing not available. Please install PyPDF2: pip install PyPDF2"
    
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_txt(txt_file):
    """Extract text from uploaded TXT file"""
    try:
        # Try different encodings
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                txt_file.seek(0)
                content = txt_file.read().decode(encoding)
                return content
            except UnicodeDecodeError:
                continue
        return "Error: Could not decode the text file"
    except Exception as e:
        return f"Error reading TXT file: {str(e)}"

def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "selected_subject" not in st.session_state:
        st.session_state.selected_subject = "Python Programming"
    if "tutor" not in st.session_state:
        st.session_state.tutor = EducationalTutor()
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []
    if "reference_content" not in st.session_state:
        st.session_state.reference_content = ""
    if "custom_subjects" not in st.session_state:
        st.session_state.custom_subjects = {}

def add_custom_subject(name: str, description: str, context: str, icon: str = "📚"):
    """Add a new custom subject to the session state"""
    if name and name not in st.session_state.custom_subjects:
        st.session_state.custom_subjects[name] = {
            "description": description or f"Custom subject: {name}",
            "context": context or f"General knowledge and concepts related to {name}",
            "icon": icon,
            "example_questions": [
                f"What are the basics of {name}?",
                f"Can you explain key concepts in {name}?",
                f"What should I know about {name}?",
                f"How can I get started with {name}?",
                f"What are common applications of {name}?"
            ],
            "study_tips": [
                "Break down complex topics into smaller parts",
                "Practice regularly and consistently",
                "Ask specific questions when you're stuck",
                "Look for real-world applications",
                "Review and summarize what you've learned"
            ],
            "custom": True  # Flag to identify custom subjects
        }
        return True
    return False

def get_all_subjects():
    """Get combined list of default and custom subjects"""
    all_subjects = dict(SUBJECTS)
    all_subjects.update(st.session_state.custom_subjects)
    return all_subjects

def display_chat_history():
    """Display the chat history in a nice format"""
    if st.session_state.chat_history:
        st.subheader("📚 Conversation History")
        
        for i, exchange in enumerate(st.session_state.chat_history):
            with st.expander(f"Q{i+1}: {exchange['question'][:50]}{'...' if len(exchange['question']) > 50 else ''}", expanded=(i == len(st.session_state.chat_history) - 1)):
                st.markdown(f"**🙋 Question:** {exchange['question']}")
                st.markdown(f"**🤖 Answer:**")
                st.markdown(exchange['answer'])
                st.markdown("---")

def main():
    # Page configuration
    st.set_page_config(**APP_CONFIG)
    
    # Apply custom styling
    apply_custom_styling()
    
    # Initialize session state
    initialize_session_state()
    
    # API Key check
    if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_gemini_api_key_here":
        st.error(UI_MESSAGES["api_key_missing"])
        return
    
    # Sidebar for subject selection and controls
    with st.sidebar:
        st.header("🎯 Subject Selection")
        
        st.markdown("---")
        
        # Subject dropdown
        all_subjects = get_all_subjects()
        selected_subject = st.selectbox(
            "Choose your subject:",
            options=list(all_subjects.keys()),
            index=list(all_subjects.keys()).index(st.session_state.selected_subject) if st.session_state.selected_subject in all_subjects else 0
        )
        
        # Update selected subject in session state
        if selected_subject != st.session_state.selected_subject:
            st.session_state.selected_subject = selected_subject
            st.rerun()
        
        # Display subject description
        subject_info = all_subjects[selected_subject]
        icon = subject_info.get('icon', '📖')
        if subject_info.get('custom', False):
            icon += " ✨"  # Add sparkle to indicate custom subject
        
        st.info(f"{icon} **About {selected_subject}:**\n\n{subject_info['description']}")
        
        # Custom Subject Creation
        with st.expander("➕ Create Custom Subject"):
            st.markdown("**Add your own subject to the tutor**")
            
            custom_name = st.text_input(
                "Subject Name:",
                placeholder="e.g., Ancient History, Machine Learning, Guitar Playing"
            )
            
            custom_description = st.text_area(
                "Description:",
                placeholder="Brief description of what this subject covers...",
                height=70
            )
            
            custom_context = st.text_area(
                "Context for AI:",
                placeholder="Detailed context to help the AI understand this subject (keywords, topics, scope)...",
                height=90
            )
            
            custom_icon = st.text_input(
                "Choose an icon:",
                value="📚",
                max_chars=2,
                placeholder="📚",
                help="Enter any emoji to represent your subject (e.g., 🎨, 🔬, 🎵, 💡)"
            )
            
            col_add, col_info = st.columns([1, 2])
            
            with col_add:
                if st.button("➕ Add Subject", type="primary", disabled=not custom_name):
                    if add_custom_subject(custom_name, custom_description, custom_context, custom_icon):
                        st.success(f"✅ Added '{custom_name}' successfully!")
                        st.session_state.selected_subject = custom_name
                        st.rerun()
                    else:
                        st.error("❌ Subject already exists or invalid name!")
            
            with col_info:
                if custom_name:
                    st.caption(f"Preview: {custom_icon} {custom_name}")
        
        # Display custom subjects management
        if st.session_state.custom_subjects:
            with st.expander("🗂️ Manage Custom Subjects"):
                for subject_name, subject_data in st.session_state.custom_subjects.items():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.text(f"{subject_data['icon']} {subject_name}")
                    with col2:
                        if st.button("🗑️", key=f"delete_subject_{subject_name}", help=f"Delete {subject_name}"):
                            del st.session_state.custom_subjects[subject_name]
                            # Switch to a default subject if current was deleted
                            if st.session_state.selected_subject == subject_name:
                                st.session_state.selected_subject = "Python Programming"
                            st.success(f"Deleted '{subject_name}'")
                            st.rerun()
        
        st.markdown("---")
        
        # File Upload Section
        st.header("📄 Reference Materials")
        
        # Determine allowed file types based on available libraries
        allowed_types = ['txt']
        if PDF_AVAILABLE:
            allowed_types.append('pdf')
        
        uploaded_files = st.file_uploader(
            f"Upload {'/'.join(allowed_types).upper()} files for reference",
            type=allowed_types,
            accept_multiple_files=True,
            help="Upload documents that the AI can reference when answering your questions"
        )
        
        if not PDF_AVAILABLE:
            st.warning("⚠️ PDF support not available. Install PyPDF2 to enable PDF uploads: `pip install PyPDF2`")
        
        # Process uploaded files
        if uploaded_files:
            all_content = ""
            processed_files = []
            
            for uploaded_file in uploaded_files:
                if uploaded_file.name not in [f["name"] for f in st.session_state.uploaded_files]:
                    # Process new file
                    with st.spinner(f"Processing {uploaded_file.name}..."):
                        if uploaded_file.type == "application/pdf":
                            content = extract_text_from_pdf(uploaded_file)
                        elif uploaded_file.type == "text/plain":
                            content = extract_text_from_txt(uploaded_file)
                        else:
                            content = "Unsupported file type"
                        
                        processed_files.append({
                            "name": uploaded_file.name,
                            "content": content,
                            "size": uploaded_file.size
                        })
                        all_content += f"\n\n--- Content from {uploaded_file.name} ---\n{content}"
            
            # Add new files to session state
            if processed_files:
                st.session_state.uploaded_files.extend(processed_files)
                st.session_state.reference_content += all_content
                st.success(f"✅ Processed {len(processed_files)} new file(s)")
        
        # Display uploaded files
        if st.session_state.uploaded_files:
            st.subheader("📚 Uploaded Files")
            for i, file_info in enumerate(st.session_state.uploaded_files):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.text(f"📄 {file_info['name']}")
                    st.caption(f"Size: {file_info['size']} bytes")
                with col2:
                    if st.button("🗑️", key=f"delete_{i}", help="Remove this file"):
                        # Remove file from session state
                        removed_file = st.session_state.uploaded_files.pop(i)
                        # Rebuild reference content without this file
                        st.session_state.reference_content = ""
                        for remaining_file in st.session_state.uploaded_files:
                            st.session_state.reference_content += f"\n\n--- Content from {remaining_file['name']} ---\n{remaining_file['content']}"
                        st.rerun()
            
            # Clear all files button
            if st.button("🗑️ Clear All Files", type="secondary"):
                st.session_state.uploaded_files = []
                st.session_state.reference_content = ""
                st.success("All files cleared!")
                st.rerun()
        
        st.markdown("---")
        
        # Chat controls
        st.header("💬 Chat Controls")
        
        if st.button("🗑️ Clear Chat History", type="secondary"):
            st.session_state.chat_history = []
            st.success(UI_MESSAGES["chat_cleared"])
            st.rerun()
        
        # Statistics
        if st.session_state.chat_history:
            st.metric("Questions Asked", len(st.session_state.chat_history))
            
            # Add export functionality
            if st.button("📥 Export Chat History"):
                export_data = export_chat_history(
                    st.session_state.chat_history, 
                    selected_subject
                )
                st.download_button(
                    label="Download JSON",
                    data=export_data,
                    file_name=f"tutor_session_{time.strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
    
    # Main content area - Full width chat interface
    
    # Show reference materials indicator
    if st.session_state.uploaded_files:
        st.info(f"📚 **Reference Materials Active**: {len(st.session_state.uploaded_files)} file(s) uploaded - The AI will use these materials to enhance responses")
    
    # Display chat history in WhatsApp-like format
    if st.session_state.chat_history:
        for i, exchange in enumerate(st.session_state.chat_history):
            if exchange["subject"] == selected_subject:
                # User message (right-aligned, green background like WhatsApp)
                st.markdown(
                    f"""
                    <div style='display: flex; justify-content: flex-end; margin: 15px 0; align-items: flex-end;'>
                        <div style='
                            background: linear-gradient(135deg, #dcf8c6 0%, #d4f4aa 100%); 
                            padding: 12px 16px; 
                            border-radius: 18px 18px 4px 18px; 
                            max-width: 80%; 
                            margin-left: 20%; 
                            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
                            position: relative;
                        '>
                            <div style='font-size: 0.85em; color: #666; margin-bottom: 6px; font-weight: 500;'>You</div>
                            <div style='color: #000; line-height: 1.4; word-wrap: break-word;'>{exchange['question']}</div>
                            <div style='font-size: 0.7em; color: #999; text-align: right; margin-top: 8px;'>
                                {format_timestamp(exchange['timestamp']).split(' ')[1]}
                            </div>
                        </div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                # AI response (left-aligned, white background like WhatsApp)
                st.markdown(
                    f"""
                    <div style='display: flex; justify-content: flex-start; margin: 15px 0; align-items: flex-end;'>
                        <div style='
                            background: white; 
                            padding: 12px 16px; 
                            border-radius: 18px 18px 18px 4px; 
                            max-width: 80%; 
                            margin-right: 20%; 
                            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
                            position: relative;
                        '>
                            <div style='font-size: 0.85em; color: #666; margin-bottom: 6px; font-weight: 500; display: flex; align-items: center;'>
                                🤖 AI Tutor
                            </div>
                            <div style='color: #000; line-height: 1.4; word-wrap: break-word;'>{exchange['answer']}</div>
                            <div style='font-size: 0.7em; color: #999; text-align: right; margin-top: 8px;'>
                                {format_timestamp(exchange['timestamp']).split(' ')[1]}
                            </div>
                        </div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
    else:
        # Empty state - no welcome message, just clean interface
        pass
    
    # Question input section
    col_input, col_submit = st.columns([5, 1])
    
    # Get the default value for the input (from selected example or empty)
    default_question = ""
    if "selected_example" in st.session_state:
        default_question = st.session_state.selected_example
        # Clear the selected example after using it
        del st.session_state.selected_example
    
    with col_input:
        question = st.text_input(
            "",
            value=default_question,
            placeholder=f"Type your message about {selected_subject}...",
            key="question_input",
            label_visibility="collapsed"
        )
    
    with col_submit:
        # Validate question before enabling submit
        question_valid, validation_msg = validate_question(question)
        submit_button = st.button("Send", type="primary", disabled=not question_valid, use_container_width=True)
    
    # Show validation message if needed
    if not question_valid and question:
        st.warning(validation_msg)
    
    # Example questions in a collapsible section
    with st.expander("💡 Need inspiration? See example questions"):
        all_subjects = get_all_subjects()
        examples = all_subjects[selected_subject].get("example_questions", ["Ask any question!"])
        for i, example in enumerate(examples):
            if st.button(f"📝 {example}", key=f"example_{hash(example)}_{i}", use_container_width=True):
                # Store the selected example in session state for the next run
                st.session_state.selected_example = example
                st.rerun()
    
    # Process question submission
    if submit_button and question_valid:
        with st.spinner(UI_MESSAGES["thinking"].format(selected_subject)):
            response = st.session_state.tutor.get_response(
                question.strip(), 
                selected_subject, 
                st.session_state.chat_history,
                st.session_state.reference_content
            )
            
            # Add to chat history
            st.session_state.chat_history.append({
                "question": question.strip(),
                "answer": response,
                "subject": selected_subject,
                "timestamp": time.time()
            })
            
            # Clear input and rerun to show new conversation
            st.rerun()
    
    # Footer
    st.markdown("---")
    
    # Display chat statistics if there's history
    if st.session_state.chat_history:
        st.subheader("📊 Session Statistics")
        display_chat_statistics(st.session_state.chat_history)
    
    # App footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; font-size: 0.9rem;'>
            🎓 AI Educational Tutor powered by Google Gemini 2.0 Flash<br>
            Built with Streamlit • Made for learning and education
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
