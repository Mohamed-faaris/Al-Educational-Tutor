# 🎓 AI Educational Tutor

A comprehensive Streamlit-based educational tutor application powered by Google's Gemini 2.0 Flash model. This application provides personalized tutoring across multiple subjects with conversation context management and interactive learning features.

## ✨ Features

- **Multi-Subject Support**: Python Programming, Basic Algebra, Calculus, Data Science, and Web Development
- **Interactive Chat Interface**: Chat-like conversation with context preservation using Gemini 2.0 Flash
- **Subject-Specific Guidance**: Tailored responses based on selected subject
- **Conversation History**: Maintains chat history with expandable conversation threads
- **Example Questions**: Built-in example questions for each subject
- **Study Tips**: Subject-specific learning tips and quick references
- **Error Handling**: Graceful handling of API errors, timeouts, and quota limits
- **Responsive UI**: Clean, modern interface with sidebar controls
- **Enhanced AI Model**: Powered by Google's latest Gemini 2.0 Flash experimental model

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google AI Studio API key (Gemini API)

### Installation

1. **Clone or download the project files**

   ```bash
   cd c:\Faaris\projects\AI-llm\tutor
   ```

2. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   - Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Open the `.env` file
   - Replace `your_gemini_api_key_here` with your actual API key:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

4. **Run the application**

   ```bash
   streamlit run app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:8501`

## 📋 Usage Guide

### Getting Started

1. **Select a Subject**: Use the dropdown in the sidebar to choose your learning topic
2. **Ask Questions**: Type your question in the text area and click "Ask Question"
3. **Review Responses**: Get detailed, educational responses with examples
4. **Continue Learning**: Ask follow-up questions to dive deeper into topics

### Features Overview

#### Subject Selection

- Choose from 5 different subjects
- Each subject has specialized context and guidance
- Subject descriptions help you understand what's covered

#### Question Input

- Large text area for detailed questions
- Example questions available for each subject
- Submit button with loading indicators

#### Chat History

- Expandable conversation threads
- Context preservation across questions
- Clear history option in sidebar

#### Study Resources

- Subject-specific study tips
- Quick reference materials
- Code examples and formulas

## 🎯 Available Subjects

### 1. Python Programming

Learn Python syntax, data structures, OOP, and best practices

- **Example Topics**: Functions, Classes, Error Handling, Libraries
- **Quick Reference**: Basic Python syntax examples

### 2. Basic Algebra

Master fundamental algebraic concepts and problem-solving

- **Example Topics**: Linear equations, Quadratic formula, Polynomials
- **Quick Reference**: Important formulas and equations

### 3. Calculus

Understand derivatives, integrals, and calculus concepts

- **Example Topics**: Limits, Derivatives, Integration, Chain Rule
- **Quick Reference**: Key calculus formulas

### 4. Data Science

Learn data analysis, statistics, and machine learning basics

- **Example Topics**: Machine Learning, Data Cleaning, Statistics
- **Quick Reference**: Common data science concepts

### 5. Web Development

Build websites with HTML, CSS, JavaScript, and frameworks

- **Example Topics**: HTML/CSS, JavaScript, React, Responsive Design
- **Quick Reference**: Web development basics

## 🔧 Technical Architecture

### Frontend (Streamlit)

- **Layout**: Two-column layout with sidebar controls
- **Components**: Dropdowns, text areas, buttons, expandable sections
- **Styling**: Custom CSS for better user experience
- **State Management**: Session state for conversation history

### Backend Integration

- **API**: Google Generative AI (Gemini 2.0 Flash experimental model)
- **Prompt Engineering**: Structured prompts with subject context
- **Context Management**: Last 5 Q&A pairs included for context
- **Error Handling**: Comprehensive error handling for various failure scenarios

### Memory Management

- **Session State**: Streamlit session state for persistence
- **Context Limitation**: Token limit management for long conversations
- **History Storage**: In-memory storage with conversation threading

## 🛠️ Prompt Engineering

The application uses sophisticated prompt engineering:

```python
system_prompt = f"""You are a helpful educational tutor specializing in {subject}.

Your role is to:
- Provide clear, detailed explanations with examples
- Break down complex concepts into understandable parts
- Offer practical examples and code snippets when relevant
- Encourage learning through guided questions
- Maintain a patient, supportive teaching style
- Focus specifically on: {subject_context}
"""
```

## ⚠️ Error Handling

The application handles various error scenarios:

- **API Quota Exceeded**: User-friendly message with retry guidance
- **Timeout Errors**: Suggestions to try shorter questions
- **Network Issues**: General error handling with details
- **Invalid API Key**: Clear setup instructions

## 🎨 UI/UX Features

### Sidebar Controls

- Subject selection dropdown
- Subject information display
- Chat history management
- Conversation statistics

### Main Interface

- Question input area
- Example question generator
- Latest response highlighting
- Comprehensive chat history

### Study Resources

- Subject-specific tips
- Quick reference materials
- Code examples and formulas

## 📊 Example Interactions

### Python Programming

```
Q: How do I create a function in Python?
A: In Python, you create a function using the `def` keyword...
```

### Basic Algebra

```
Q: What is the quadratic formula?
A: The quadratic formula is used to solve quadratic equations...
```

## 🔒 Security

- **Environment Variables**: API keys stored in `.env` file
- **Input Validation**: Basic input sanitization
- **Error Messages**: Safe error handling without exposing sensitive information

## 📈 Future Enhancements

Potential improvements for the application:

1. **User Authentication**: User accounts and personalized learning paths
2. **Progress Tracking**: Learning progress and achievement system
3. **Export Features**: Save conversations and study materials
4. **Additional Subjects**: More subjects like Physics, Chemistry, History
5. **Voice Integration**: Speech-to-text and text-to-speech capabilities
6. **Mobile Optimization**: Enhanced mobile experience
7. **Collaborative Learning**: Shared study sessions and peer learning

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **API Key Error**

   - Ensure your API key is correctly set in `.env`
   - Check that you have API quota remaining

2. **Installation Issues**

   - Verify Python version (3.8+)
   - Try upgrading pip: `pip install --upgrade pip`

3. **Port Issues**

   - If port 8501 is busy, Streamlit will automatically use another port
   - Check the terminal output for the correct URL

4. **Performance Issues**
   - Clear chat history if conversations become very long
   - Restart the application if memory usage is high

### Getting Help

If you encounter issues:

1. Check the error messages in the application
2. Review the console output when running the app
3. Ensure all dependencies are properly installed
4. Verify your internet connection for API calls

## 📞 Support

For support and questions:

- Review this README thoroughly
- Check the application's built-in error messages
- Consult the Streamlit and Google AI documentation
