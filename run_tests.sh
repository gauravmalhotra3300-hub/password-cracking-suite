#!/bin/bash
# Quick test runner for password-cracking-suite
set -e
echo 'Setting up Kali Linux test environment'
if [ ! -d venv ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt -q
python3 -m unittest test_password_analyzer -v
