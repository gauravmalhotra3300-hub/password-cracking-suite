# Password Cracking & Credential Attack Suite


![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![GitHub Actions](https://github.com/gauravmalhotra3300-hub/password-cracking-suite/workflows/Python%20CI/CD/badge.svg) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-stable-brightgreen)
A comprehensive toolkit for ethical password policy testing and credential security assessment.

## Features
- Dictionary Generator: Custom wordlist generation with mutations
- Hash Extractor Demo: Educational demonstration of hash extraction
- Brute-Force Simulator: Time-to-crack estimation
- Password Strength Analyzer: Entropy and complexity analysis
- Report Generator: Security audit reports

## Usage

```bash
python3 main.py --help
python3 main.py --analyze 'MyPassword123'
python3 main.py --generate-wordlist john 1990 wordlists/john.txt

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![GitHub Actions](https://github.com/gauravmalhotra3300-hub/password-cracking-suite/workflows/Python%20CI/CD/badge.svg) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-stable-brightgreen)
python3 main.py --extract-hashes reports/hashes.json

