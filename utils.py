"""
Utility functions for the AI Educational Tutor application.
"""

import streamlit as st
import time
from datetime import datetime
from typing import List, Dict, Any
import json
import os

def format_timestamp(timestamp: float) -> str:
    """Format timestamp for display"""
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def count_tokens_estimate(text: str) -> int:
    """Rough estimate of tokens in text (approximately 4 characters per token)"""
    return len(text) // 4

def export_chat_history(chat_history: List[Dict], subject: str) -> str:
    """Export chat history to JSON format"""
    export_data = {
        "subject": subject,
        "export_timestamp": datetime.now().isoformat(),
        "total_questions": len(chat_history),
        "conversations": []
    }
    
    for i, exchange in enumerate(chat_history):
        export_data["conversations"].append({
            "question_number": i + 1,
            "question": exchange["question"],
            "answer": exchange["answer"],
            "subject": exchange["subject"],
            "timestamp": format_timestamp(exchange["timestamp"])
        })
    
    return json.dumps(export_data, indent=2)

def validate_question(question: str) -> tuple[bool, str]:
    """Validate user question input"""
    if not question or not question.strip():
        return False, "Please enter a question before submitting."
    
    if len(question.strip()) < 3:
        return False, "Please enter a more detailed question."
    
    if len(question.strip()) > 1000:
        return False, "Question is too long. Please keep it under 1000 characters."
    
    return True, ""

def display_loading_animation():
    """Display a loading animation"""
    with st.empty():
        for i in range(3):
            st.text("Thinking" + "." * (i + 1))
            time.sleep(0.5)

def safe_get_subject_info(subjects: Dict, subject: str, key: str, default: Any = None):
    """Safely get subject information with fallback"""
    return subjects.get(subject, {}).get(key, default)

def create_download_link(data: str, filename: str, mime_type: str = "text/plain") -> str:
    """Create a download link for data"""
    import base64
    b64 = base64.b64encode(data.encode()).decode()
    return f'<a href="data:{mime_type};base64,{b64}" download="{filename}">Download {filename}</a>'

def display_chat_statistics(chat_history: List[Dict]) -> None:
    """Display statistics about the chat session"""
    if not chat_history:
        return
    
    total_questions = len(chat_history)
    subjects_used = set(exchange.get("subject", "Unknown") for exchange in chat_history)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Questions", total_questions)
    
    with col2:
        st.metric("Subjects Explored", len(subjects_used))
    
    with col3:
        if chat_history:
            session_duration = chat_history[-1]["timestamp"] - chat_history[0]["timestamp"]
            st.metric("Session Duration", f"{int(session_duration // 60)}m {int(session_duration % 60)}s")

def get_conversation_summary(chat_history: List[Dict]) -> str:
    """Generate a summary of the conversation"""
    if not chat_history:
        return "No conversation yet."
    
    total_questions = len(chat_history)
    subjects = list(set(exchange.get("subject", "Unknown") for exchange in chat_history))
    
    summary = f"Session Summary:\n"
    summary += f"• {total_questions} question{'s' if total_questions != 1 else ''} asked\n"
    summary += f"• Subject{'s' if len(subjects) != 1 else ''}: {', '.join(subjects)}\n"
    
    if chat_history:
        start_time = format_timestamp(chat_history[0]["timestamp"])
        end_time = format_timestamp(chat_history[-1]["timestamp"])
        summary += f"• Session: {start_time} to {end_time}"
    
    return summary

class SessionManager:
    """Manage session state and persistence"""
    
    @staticmethod
    def save_session(chat_history: List[Dict], filename: str = None) -> bool:
        """Save session to file"""
        try:
            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"tutor_session_{timestamp}.json"
            
            session_data = {
                "saved_at": datetime.now().isoformat(),
                "chat_history": chat_history
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            st.error(f"Failed to save session: {str(e)}")
            return False
    
    @staticmethod
    def load_session(filename: str) -> List[Dict]:
        """Load session from file"""
        try:
            if not os.path.exists(filename):
                return []
            
            with open(filename, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
            
            return session_data.get("chat_history", [])
        except Exception as e:
            st.error(f"Failed to load session: {str(e)}")
            return []

def display_subject_icon(subject: str, subjects: Dict) -> str:
    """Get the icon for a subject"""
    return safe_get_subject_info(subjects, subject, "icon", "📚")

def format_response_with_sections(response: str) -> str:
    """Format AI response with better section headers"""
    # This could be enhanced to parse and format different sections
    # For now, just return the response as-is
    return response

def check_api_health() -> bool:
    """Check if the API is accessible"""
    try:
        import google.generativeai as genai
        # This is a simple check - in a real app you might want to make a test request
        return True
    except Exception:
        return False
