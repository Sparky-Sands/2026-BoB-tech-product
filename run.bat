@echo off
echo Starting Build Process for LLM Accuracy Tracker...

:: Install required Python packages
echo Installing dependencies (streamlit, pandas)...
pip install streamlit pandas

:: Check if installation was successful
if %errorlevel% neq 0 (
    echo Error installing dependencies. Please check your Python/Pip installation.
    pause
    exit /b %errorlevel%
)

echo Dependencies installed successfully.
echo Starting the Streamlit application...

:: NOTE: Make sure "Project-Mockup.py" matches the exact name of your python file!
streamlit run Project-Mockup.py

pause
