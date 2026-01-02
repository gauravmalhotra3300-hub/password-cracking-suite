#!/usr/bin/env python3
import argparse
from dictionary_generator import DictionaryGenerator
from hash_extractor_demo import HashExtractorDemo
from bruteforce_simulator import BruteforceSimulator
from password_analyzer import PasswordAnalyzer
from report_generator import ReportGenerator

class PasswordCrackingSuite:
    def __init__(self):
        self.dict_gen = DictionaryGenerator()
        self.hash_extractor = HashExtractorDemo()
        self.bruteforce = BruteforceSimulator()
        self.analyzer = PasswordAnalyzer()
        self.reporter = ReportGenerator()
    
    def analyze_password(self, password):
        result = self.analyzer.analyze_password(password)
        print(f"\n{'='*60}")
        print(f"Password Analysis: {password}")
        print(f"{'='*60}")
        print(f"Length: {result['password_length']}")
        print(f"Has Lowercase: {result['has_lowercase']}")
        print(f"Has Uppercase: {result['has_uppercase']}")
        print(f"Has Digits: {result['has_digits']}")
        print(f"Entropy: {result['entropy']} bits")
        print(f"Strength: {result['strength']}")
        print(f"Recommendations:")
        for rec in result['recommendations']:
            print(f"  • {rec}")
    
    def generate_wordlist(self, name, dob, output):
        wordlist = self.dict_gen.generate_pattern_based(name, dob)
        count = self.dict_gen.save_to_file(wordlist, output)
        print(f"✓ Generated {count} passwords in {output}")
    
    def extract_hashes(self, output):
        hashes = self.hash_extractor.generate_demo_hashes()
        self.hash_extractor.export_hashes_json(hashes['shadow_hashes'], output)
        print(f"✓ Extracted hashes to {output}")

def main():
    parser = argparse.ArgumentParser(description='Password Cracking Suite')
    parser.add_argument('--analyze', type=str, help='Analyze password')
    parser.add_argument('--generate-wordlist', nargs=3, help='Generate wordlist')
    parser.add_argument('--extract-hashes', type=str, help='Extract hashes')
    
    args = parser.parse_args()
    suite = PasswordCrackingSuite()
    
    if args.analyze:
        suite.analyze_password(args.analyze)
    elif args.generate_wordlist:
        suite.generate_wordlist(args.generate_wordlist[0], args.generate_wordlist[1], args.generate_wordlist[2])
    elif args.extract_hashes:
        suite.extract_hashes(args.extract_hashes)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
