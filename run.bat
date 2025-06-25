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
    echo.
    echo ======================================
    echo          SETUP REQUIRED
    echo ======================================
    echo ERROR: .env file not found!
    echo.
    echo To use this application, you need a Gemini API key.
    echo.
    echo Steps to set up:
    echo 1. Get your FREE Gemini API key from:
    echo    https://makersuite.google.com/app/apikey
    echo.
    echo 2. Copy the .env.sample file to .env:
    echo    copy .env.sample .env
    echo.
    echo 3. Edit the .env file and replace "your_gemini_api_key_here"
    echo    with your actual API key
    echo.
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

REM Check if API key is still the placeholder
findstr /c:"your_gemini_api_key_here" .env >nul
if %errorlevel% equ 0 (
    echo.
    echo ======================================
    echo       API KEY SETUP REQUIRED
    echo ======================================
    echo WARNING: Please update your Gemini API key in the .env file
    echo.
    echo Your .env file still contains the placeholder value.
    echo.
    echo Steps to fix:
    echo 1. Get your FREE Gemini API key from:
    echo    https://makersuite.google.com/app/apikey
    echo.
    echo 2. Open the .env file in a text editor
    echo.
    echo 3. Replace "your_gemini_api_key_here" with your actual API key
    echo.
    echo 4. Save the file and run this script again
    echo.
    pause
    exit /b 1
)

REM Check if API key exists and is not empty
findstr /r "^GOOGLE_API_KEY=...*" .env >nul
if %errorlevel% neq 0 (
    echo.
    echo ======================================
    echo       INVALID API KEY FORMAT
    echo ======================================
    echo ERROR: Invalid or missing Gemini API key in .env file
    echo.
    echo Please ensure your .env file contains:
    echo GOOGLE_API_KEY=your_actual_api_key_here
    echo.
    echo Get your FREE Gemini API key from:
    echo https://makersuite.google.com/app/apikey
    echo.
    pause
    exit /b 1
)

echo.
echo Starting AI Educational Tutor...
echo.
echo The application will open in your default web browser.
echo Press Ctrl+C to stop the application.
echo.

streamlit run app.py

pause
