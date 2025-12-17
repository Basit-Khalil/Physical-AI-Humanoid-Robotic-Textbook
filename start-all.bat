@echo off
echo Starting AI-Native Software Development Book Project...
echo.

echo Step 1: Starting Qdrant Vector Database...
start cmd /k "cd /d %~dp0 && docker-compose up"

timeout /t 5 /nobreak >nul

echo Step 2: Starting Backend Server...
start cmd /k "cd /d %~dp0\backend && python main.py"

timeout /t 5 /nobreak >nul

echo Step 3: Starting Frontend Server (Port 3001)...
start cmd /k "cd /d %~dp0\book && npx docusaurus start --port 3001"

echo.
echo All services started!
echo - Qdrant: http://localhost:6333 (requires Docker)
echo - Backend: http://localhost:8001
echo - Frontend: http://localhost:3001
echo.
echo Note: Make sure you have Docker running for Qdrant, and Python dependencies installed.
pause