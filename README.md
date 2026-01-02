# Password Cracking & Credential Attack Suite

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
python3 main.py --extract-hashes reports/hashes.json

