@echo off
echo Starting Skin Cancer Classification System...
echo.

REM Check if migrations are needed
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo Starting Django development server...
echo.
echo Access the application at: http://127.0.0.1:8000/
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
