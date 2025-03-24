#!/bin/bash

echo "BUILD START"

# Check if python3.11 is installed, if not install it
if ! command -v python3.11 &> /dev/null
then
    echo "Python 3.11 not found, installing..."
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv python3.11-dev
fi

# Ensure pip is up to date
python3.11 -m ensurepip --upgrade
python3.11 -m pip install --upgrade pip

# Install dependencies
python3.11 -m pip install -r requirements.txt

# Run Django setup commands
python3.11 manage.py makemigrations --noinput
python3.11 manage.py migrate --noinput
python3.11 manage.py collectstatic --noinput --clear

echo "BUILD END"
