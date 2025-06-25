@echo off
echo.
echo ======================================
echo   AI Educational Tutor Application
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher and try again
    pause
    exit /b 1
)

echo Python version:
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing/updating dependencies...
pip install -r requirements.txt
echo.

REM Check if .env file exists and has API key
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please create a .env file with your Gemini API key
    pause
    exit /b 1
)

findstr /c:"your_gemini_api_key_here" .env >nul
if %errorlevel% equ 0 (
    echo.
    echo WARNING: Please update your API key in the .env file
    echo Get your API key from: https://makersuite.google.com/app/apikey
    echo.
    pause
)

echo.
echo Starting AI Educational Tutor...
echo.
echo The application will open in your default web browser.
echo Press Ctrl+C to stop the application.
echo.

streamlit run app.py

pause
