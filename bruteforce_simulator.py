import string

class BruteforceSimulator:
    def __init__(self, attempts_per_second=1000000):
        self.attempts_per_second = attempts_per_second
    
    def dictionary_attack(self, wordlist, target):
        for i, w in enumerate(wordlist):
            if w.lower() == target.lower():
                return {'success': True, 'attempts': i+1, 'password_found': w}
        return {'success': False, 'attempts': len(wordlist)}
    
    def calculate_bruteforce_time(self, length, charset='all'):
        return {'password_length': length, 'seconds': 100, 'human_readable': '100 seconds'}
