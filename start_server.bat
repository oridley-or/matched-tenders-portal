@echo off
REM Activate the virtual environment
call venv\Scripts\activate

REM Run the app in production mode (no --reload)
uvicorn app.main:app --host 0.0.0.0 --port 8000

REM Keep terminal open after shutdown
pause
