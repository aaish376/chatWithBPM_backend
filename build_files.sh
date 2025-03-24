#!/bin/bash

echo "BUILD START"

# Check Python version
python3 --version

# Create virtual environment if not exists
python3 -m venv venv

# Activate the virtual environment (adjust for Vercel)
export VIRTUAL_ENV=$(pwd)/venv
export PATH=$VIRTUAL_ENV/bin:$PATH

# Confirm the correct Python path
echo "Using Python: $(which python3)"
echo "Using Pip: $(which pip)"

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installed packages
pip list | grep Django

# Run Django setup commands
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
