#!/bin/bash

echo "🔧 Setting up ClubOS Lite..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Dependencies installed."
echo "🚀 Starting server..."
uvicorn backend.main:app --reload