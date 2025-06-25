# AI Educational Tutor - Installation Guide

## Quick Start (Windows)

### Option 1: Use the Batch Script (Recommended)

1. **Download/clone the project files** to your desired directory
2. **Get your Gemini API key** from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Copy `.env.sample` to `.env`** and update with your API key
4. **Double-click `run.bat`** - this will automatically:
   - Create a virtual environment
   - Install all dependencies
   - Start the application

### Option 2: Manual Installation

Follow these steps if you prefer manual setup:

```bash
# 1. Navigate to the project directory
cd ai-educational-tutor

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy and update .env file with your API key
copy .env.sample .env
# (Edit .env file and replace your_gemini_api_key_here with actual key)

# 5. Run the application
streamlit run app.py
```

## Prerequisites

### System Requirements

- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.8 or higher
- **Internet Connection**: Required for API calls
- **Web Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)

### Required Python Packages

All packages are listed in `requirements.txt`:

- `streamlit>=1.28.0` - Web application framework
- `google-generativeai>=0.3.0` - Google Gemini API client
- `python-dotenv>=1.0.0` - Environment variable management

## API Setup

### Getting Your Gemini API Key

1. **Visit Google AI Studio**: Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. **Sign in** with your Google account
3. **Create API Key**: Click "Create API Key" button
4. **Copy the key**: Save it securely - you won't be able to see it again
5. **Update .env file**: Replace `your_gemini_api_key_here` with your actual key

### API Limits and Pricing

- **Free Tier**: Google provides free usage with rate limits
- **Rate Limits**: Check current limits at [Google AI Studio](https://makersuite.google.com/)
- **Pricing**: Review pricing at [Google AI Pricing](https://cloud.google.com/vertex-ai/pricing)

## Project Structure

```
ai-educational-tutor/
├── app.py              # Main Streamlit application
├── config.py           # Configuration and subjects data
├── utils.py            # Utility functions
├── styles.py           # Custom CSS styling
├── requirements.txt    # Python dependencies
├── .env.sample         # Environment variables template
├── .env               # Environment variables (API key) - created by user
├── run.bat            # Windows startup script
├── README.md          # Project documentation
└── INSTALL.md         # This installation guide
```

## Configuration

### Environment Variables (.env file)

```bash
# Required: Your Gemini API key
GOOGLE_API_KEY=your_actual_api_key_here

# Optional: Additional configuration
# STREAMLIT_SERVER_PORT=8501
# STREAMLIT_SERVER_ADDRESS=localhost
```

### Application Settings (config.py)

You can customize the application by editing `config.py`:

- **Add new subjects**: Extend the `SUBJECTS` dictionary
- **Modify API settings**: Adjust `API_CONFIG` parameters
- **Update UI messages**: Customize `UI_MESSAGES`
- **Change prompts**: Modify `SYSTEM_PROMPT_TEMPLATE`

## Running the Application

### Method 1: Batch Script (Windows Only)

```bash
# Simply double-click run.bat or execute in command prompt
run.bat
```

### Method 2: Direct Streamlit Command

```bash
# Activate virtual environment first
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Run the application
streamlit run app.py
```

### Method 3: Python Module

```bash
# From the project directory
python -m streamlit run app.py
```

## Accessing the Application

Once started, the application will:

1. **Open automatically** in your default web browser
2. **Display the URL** in the terminal (usually http://localhost:8501)
3. **Show any startup errors** in the terminal

### Manual Access

If the browser doesn't open automatically:

1. Open your web browser
2. Navigate to `http://localhost:8501`
3. The application should load

## Troubleshooting

### Common Issues and Solutions

#### 1. Python Not Found

```
Error: Python is not installed or not in PATH
```

**Solution**:

- Install Python 3.8+ from [python.org](https://python.org)
- Ensure "Add to PATH" is checked during installation
- Restart command prompt after installation

#### 2. API Key Error

```
Error: API Key Required
```

**Solution**:

- Verify `.env` file exists in the project directory
- Check that API key is correctly set (no extra spaces)
- Ensure API key is valid and active

#### 3. Package Installation Fails

```
Error: Could not install packages
```

**Solution**:

- Update pip: `python -m pip install --upgrade pip`
- Use virtual environment: `python -m venv venv`
- Try installing packages individually

#### 4. Port Already in Use

```
Error: Port 8501 is already in use
```

**Solution**:

- Streamlit will automatically find another port
- Check terminal output for the correct URL
- Or specify a different port: `streamlit run app.py --server.port 8502`

#### 5. API Quota Exceeded

```
Warning: API Quota Exceeded
```

**Solution**:

- Wait for quota reset (usually daily)
- Check your API usage at [Google AI Studio](https://makersuite.google.com/)
- Consider upgrading your API plan if needed

#### 6. Slow Response Times

**Solution**:

- Check your internet connection
- Try shorter questions
- Clear chat history to reduce context length

### Getting Help

If you encounter issues not covered here:

1. **Check the terminal output** for detailed error messages
2. **Verify all files are present** and in correct locations
3. **Ensure Python version is 3.8+**: `python --version`
4. **Check API key validity** at Google AI Studio
5. **Try in a fresh virtual environment**

### Support Resources

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **Google AI Documentation**: [ai.google.dev](https://ai.google.dev)
- **Python Virtual Environments**: [docs.python.org](https://docs.python.org/3/tutorial/venv.html)

## Development Setup

### For Developers

If you want to modify or extend the application:

```bash
# 1. Clone/download the project
git clone <repository-url>
cd ai-educational-tutor

# 2. Create development environment
python -m venv dev-env
dev-env\Scripts\activate  # Windows
# or
source dev-env/bin/activate  # macOS/Linux

# 3. Install dependencies with development tools
pip install -r requirements.txt
pip install streamlit-dev-tools  # Optional: for development

# 4. Install in development mode
pip install -e .

# 5. Run with auto-reload
streamlit run app.py --server.runOnSave true
```

### Code Structure

- **app.py**: Main application entry point
- **config.py**: All configuration and constants
- **utils.py**: Helper functions and utilities
- **styles.py**: CSS styling and theming

### Adding New Features

1. **New Subjects**: Add to `SUBJECTS` in `config.py`
2. **New UI Components**: Add to `app.py` with styling in `styles.py`
3. **New Utilities**: Add to `utils.py`
4. **Configuration**: Update `config.py`

## Security Notes

### API Key Security

- **Never commit** `.env` files to version control
- **Use environment variables** in production
- **Rotate keys regularly** for security
- **Monitor usage** to detect unauthorized use

### Application Security

- Application runs locally by default
- No user data is stored permanently
- All chat history is session-based
- API calls are made directly to Google's servers

## Performance Optimization

### Tips for Better Performance

1. **Clear chat history** when conversations get very long
2. **Use shorter questions** for faster responses
3. **Restart application** if memory usage gets high
4. **Close unused browser tabs** to free resources

### Monitoring Usage

- Check API usage at Google AI Studio
- Monitor response times in the application
- Watch for quota warnings in the UI

## Next Steps

After successful installation:

1. **Test the application** with example questions
2. **Explore different subjects** to understand capabilities
3. **Try various question types** (explanations, examples, practice problems)
4. **Use the export feature** to save important conversations
5. **Customize subjects** by editing `config.py` if needed

Enjoy learning with your AI Educational Tutor! 🎓
