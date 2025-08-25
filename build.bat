@echo off
REM Script para empaquetar el juego en Windows

REM 1. Instalar dependencias
pip install -r requirements.txt

REM 2. Limpiar builds anteriores
rmdir /s /q build dist __pycache__

REM 3. Crear el ejecutable
pyinstaller --onefile juego.py

echo Ejecutable generado en dist\juego.exe
pause