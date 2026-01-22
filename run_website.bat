@echo off
REM Navigate to your project folder
cd /d "C:\Users\raja5\Desktop\ai_resume_screening"

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run Flask app
python app.py

pause