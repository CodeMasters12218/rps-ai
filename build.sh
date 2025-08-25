#!/bin/bash
# Script para empaquetar el juego en Linux/Mac

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Limpiar builds anteriores
rm -rf build dist __pycache__

# 3. Crear ejecutable
pyinstaller --onefile juego.py

echo "Ejecutable generado en dist/juego"