#!/bin/bash

echo "Starting Weather Dashboard Backend..."
echo

cd backend

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Starting backend server..."
python run.py
