"""
Custom styling for the AI Educational Tutor application.
"""

def get_custom_css():
    """Return custom CSS for the application"""
    return """
    <style>
    /* Main app styling */
    .main {
        padding-top: 1rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Chat message styling - WhatsApp-like */
    .chat-message {
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        max-width: 70%;
        word-wrap: break-word;
    }
    
    .user-message {
        background-color: #DCF8C6;
        margin-left: auto;
        margin-right: 0;
        border-radius: 15px 15px 5px 15px;
    }
    
    .ai-message {
        background-color: #f1f1f1;
        margin-left: 0;
        margin-right: auto;
        border-radius: 15px 15px 15px 5px;
    }
    
    /* Chat container styling */
    .chat-container {
        height: 400px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #fafafa;
        margin-bottom: 20px;
    }
    
    /* Input styling for chat */
    .stTextInput input {
        border-radius: 25px;
        border: 2px solid #e0e0e0;
        padding: 10px 15px;
        font-size: 16px;
    }
    
    .stTextInput input:focus {
        border-color: #25D366;
        box-shadow: 0 0 0 2px rgba(37, 211, 102, 0.25);
    }
    
    /* Subject card styling */
    .subject-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
    }
    
    /* Button styling - Modern blue theme */
    .stButton > button {
        background: #007bff;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: #0056b3;
        color: #f8f9fa;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Send button specific styling */
    .stButton button[kind="primary"] {
        background: #007bff;
        border-radius: 50%;
        width: 50px;
        height: 40px;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Metrics styling */
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Code block styling */
    .stCodeBlock {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background-color: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
        border-radius: 8px;
    }
    
    .stError {
        background-color: #f8d7da;
        border-color: #f5c6cb;
        color: #721c24;
        border-radius: 8px;
    }
    
    .stInfo {
        background-color: #d1ecf1;
        border-color: #bee5eb;
        color: #0c5460;
        border-radius: 8px;
    }
    
    /* Loading spinner styling */
    .stSpinner {
        text-align: center;
        color: #667eea;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-radius: 5px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main {
            padding: 0.5rem;
        }
        
        .chat-message {
            padding: 0.75rem;
        }
        
        .main-header {
            padding: 0.75rem;
        }
    }
    
    /* Text input styling */
    .stTextArea textarea {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.25);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.25);
    }
    
    /* Progress bar styling */
    .stProgress .st-bo {
        background-color: #667eea;
    }
    
    /* Custom classes for dynamic content */
    .question-highlight {
        background: linear-gradient(120deg, #a8e6cf 0%, #dcedc8 100%);
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    
    .answer-highlight {
        background: linear-gradient(120deg, #ffcccb 0%, #ffb3ba 100%);
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    
    .subject-badge {
        background: #667eea;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    </style>
    """

def apply_custom_styling():
    """Apply custom CSS to the Streamlit app"""
    import streamlit as st
    st.markdown(get_custom_css(), unsafe_allow_html=True)
