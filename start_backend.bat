@echo off
echo Starting Weather Dashboard Backend...
echo.

cd backend

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting backend server...
python run.py

pause
