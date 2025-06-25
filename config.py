"""
Configuration file for the AI Educational Tutor application.
This file contains all the configurable settings and constants.
"""

# Application Configuration
APP_CONFIG = {
    "page_title": "AI Educational Tutor",
    "page_icon": "🎓",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# API Configuration
API_CONFIG = {
    "model_name": "gemini-2.0-flash-exp",
    "max_chat_history": 5,  # Number of previous Q&A pairs to include in context
    "max_tokens": 8192,     # Maximum tokens for the model
    "temperature": 0.7      # Response creativity (0.0 to 1.0)
}

# Subject Configuration
SUBJECTS = {
    "Python Programming": {
        "description": "Learn Python programming concepts, syntax, and best practices",
        "context": "Python programming language including syntax, data structures, algorithms, object-oriented programming, and libraries",
        "icon": "🐍",
        "example_questions": [
            "How do I create a class in Python?",
            "What's the difference between lists and tuples?",
            "How do I handle exceptions in Python?",
            "How do I work with files in Python?",
            "What are Python decorators and how do I use them?"
        ],
        "study_tips": [
            "Practice coding daily for at least 30 minutes",
            "Read error messages carefully - they often tell you exactly what's wrong",
            "Use the Python documentation as a reference",
            "Try to understand concepts, don't just memorize syntax",
            "Build small projects to apply what you learn"
        ],
        "quick_reference": {
            "type": "code",
            "language": "python",
            "content": """# Python Basics
print("Hello World")
variable = "value"
my_list = [1, 2, 3]
my_dict = {"key": "value"}

# Function
def my_function(param):
    return param * 2

# Class
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value"""
        }
    },
    "Basic Algebra": {
        "description": "Master fundamental algebraic concepts and problem-solving",
        "context": "Basic algebra including linear equations, quadratic equations, polynomials, factoring, and algebraic expressions",
        "icon": "📐",
        "example_questions": [
            "How do I solve linear equations?",
            "What is the quadratic formula?",
            "How do I factor polynomials?",
            "What are the properties of exponents?",
            "How do I graph linear functions?"
        ],
        "study_tips": [
            "Practice solving different types of problems regularly",
            "Check your work by substituting answers back into equations",
            "Keep a formula sheet for quick reference",
            "Break complex problems into smaller steps",
            "Understand the 'why' behind each step"
        ],
        "quick_reference": {
            "type": "latex",
            "content": r"""
\text{Quadratic Formula:}\\
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\\
\\
\text{Slope Formula:}\\
m = \frac{y_2 - y_1}{x_2 - x_1}\\
\\
\text{Distance Formula:}\\
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
"""
        }
    },
    "Calculus": {
        "description": "Understand derivatives, integrals, and calculus concepts",
        "context": "Calculus including limits, derivatives, integrals, differential equations, and applications",
        "icon": "∫",
        "example_questions": [
            "What is a derivative?",
            "How do I find the integral of a function?",
            "What is the chain rule?",
            "How do I find limits?",
            "What are applications of derivatives in real life?"
        ],
        "study_tips": [
            "Master the fundamentals before moving to advanced topics",
            "Practice graphing functions to visualize concepts",
            "Use online graphing tools to check your work",
            "Work through many practice problems",
            "Connect calculus concepts to real-world applications"
        ],
        "quick_reference": {
            "type": "latex",
            "content": r"""
\text{Power Rule:}\\
\frac{d}{dx}[x^n] = nx^{n-1}\\
\\
\text{Chain Rule:}\\
\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)\\
\\
\text{Fundamental Theorem:}\\
\int_a^b f'(x)dx = f(b) - f(a)
"""
        }
    },
    "Data Science": {
        "description": "Learn data analysis, statistics, and machine learning basics",
        "context": "Data science including statistics, data analysis, machine learning, data visualization, and Python libraries like pandas, numpy, and scikit-learn",
        "icon": "📊",
        "example_questions": [
            "What is the difference between supervised and unsupervised learning?",
            "How do I clean messy data?",
            "What is cross-validation?",
            "How do I interpret correlation vs causation?",
            "What are the steps in a data science project?"
        ],
        "study_tips": [
            "Practice with real datasets",
            "Learn to ask the right questions about data",
            "Understand statistics before diving into machine learning",
            "Document your analysis process",
            "Focus on interpreting results, not just running algorithms"
        ],
        "quick_reference": {
            "type": "code",
            "language": "python",
            "content": """# Data Science Basics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Basic exploration
df.head()
df.info()
df.describe()

# Data cleaning
df.dropna()
df.fillna(value)

# Visualization
plt.scatter(df['x'], df['y'])
plt.show()"""
        }
    },
    "Web Development": {
        "description": "Build websites with HTML, CSS, JavaScript, and frameworks",
        "context": "Web development including HTML, CSS, JavaScript, React, Node.js, and web technologies",
        "icon": "🌐",
        "example_questions": [
            "What's the difference between HTML and CSS?",
            "How do I make a responsive website?",
            "What is the DOM in JavaScript?",
            "How do I center a div?",
            "What are the benefits of using a framework like React?"
        ],
        "study_tips": [
            "Build projects to apply what you learn",
            "Use browser developer tools to debug",
            "Stay updated with web standards and best practices",
            "Practice responsive design from the start",
            "Learn version control (Git) early"
        ],
        "quick_reference": {
            "type": "code",
            "language": "html",
            "content": """<!-- HTML Structure -->
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <style>
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World</h1>
    </div>
    
    <script>
        document.querySelector('h1')
            .addEventListener('click', 
                () => alert('Hello!'));
    </script>
</body>
</html>"""
        }
    }
}

# UI Messages
UI_MESSAGES = {
    "api_key_missing": """
⚠️ **API Key Required**: Please set your Gemini API key in the `.env` file to use this application.

**Steps to get started:**
1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Replace `your_gemini_api_key_here` in the `.env` file with your actual API key
3. Restart the application
""",
    "quota_exceeded": "⚠️ **API Quota Exceeded**: The API request limit has been reached. Please try again later.",
    "timeout_error": "⚠️ **Timeout Error**: The request took too long to process. Please try again with a shorter question.",
    "general_error": "⚠️ **Error**: Unable to process your request. Please check your API key and try again.",
    "chat_cleared": "Chat history cleared!",
    "thinking": "🤔 Thinking about your {} question...",
    "no_question": "Please enter a question before submitting."
}

# System Prompt Template optimized for Gemini 2.0 Flash
SYSTEM_PROMPT_TEMPLATE = """You are an expert educational tutor specializing in {subject}, powered by advanced AI to provide the best learning experience.

Your mission is to:
- Deliver crystal-clear, comprehensive explanations with practical examples
- Break down complex concepts into digestible, sequential steps
- Provide hands-on code snippets, formulas, and visual representations when relevant
- Ask thought-provoking follow-up questions to deepen understanding
- Maintain an encouraging, patient, and adaptive teaching approach
- Focus exclusively on: {subject_context}

Teaching methodology:
- Begin with foundational concepts and progressively build complexity
- Use relatable analogies and real-world applications to illustrate abstract ideas
- Structure responses with clear headings and bullet points for easy scanning
- Include practical exercises and mini-challenges when appropriate
- Provide multiple learning approaches (visual, analytical, hands-on) for different learning styles
- Format all responses using rich Markdown for optimal readability

Response structure:
1. **Quick Answer**: Brief, direct response to the question
2. **Detailed Explanation**: Step-by-step breakdown with examples
3. **Practical Application**: Real-world usage or coding examples
4. **Practice Suggestion**: A small exercise or next step for the learner
5. **Related Concepts**: Brief mention of connected topics to explore

Communication style:
- Use encouraging, supportive language that builds confidence
- Acknowledge when concepts are challenging and normalize the learning process
- If a question is outside the subject scope, kindly redirect with relevant alternatives
- Celebrate learning progress and encourage curiosity
- Adapt explanations based on the apparent skill level shown in questions

Special instructions for custom subjects:
- If this appears to be a custom or specialized subject, be extra attentive to the provided context
- Ask clarifying questions if the subject area seems unclear
- Draw connections to more established fields when helpful
- Be creative in finding analogies and examples for unique topics
"""

# Default icons for quick selection
SUBJECT_ICONS = [
    "📚", "🎨", "🔬", "🎵", "🏛️", "⚖️", "🌱", "🍳", 
    "🏃", "💼", "🎭", "🔧", "🎯", "🌟", "🔮", "🎪",
    "🏺", "🎲", "📸", "🌍", "🚀", "💡", "🎬", "📊"
]
