import random
from typing import List

class DictionaryGenerator:
    def __init__(self):
        self.mutations = {'a': ['@', '4'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['5', '$']}
    
    def generate_pattern_based(self, name, dob=None, appends=None):
        wordlist = set([name, name.upper(), name.capitalize()])
        if dob:
            wordlist.add(f"{name}{dob}")
            wordlist.add(f"{dob}{name}")
        return list(wordlist)
    
    def save_to_file(self, wordlist, filename):
        unique = list(set(wordlist))
        with open(filename, 'w') as f:
            for w in unique:
                f.write(w + "\n")
        return len(unique)
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                return [line.strip() for line in f]
        except:
            return []
