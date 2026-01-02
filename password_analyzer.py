"""
Password Strength Analyzer Module
Analyzes password strength based on complexity, entropy, and predictability.
"""

import math
import re


class PasswordAnalyzer:
    """
    Analyzes and rates password strength.
    
    Features:
    - Complexity checking (uppercase, lowercase, digits, symbols)
    - Shannon entropy calculation
    - Dictionary weakness detection
    - Security recommendations
    """
    
    def __init__(self):
        """Initialize analyzer with common weak passwords."""
        self.weak_passwords = [
            'password', 'admin', '123456', 'qwerty', 'letmein', 'welcome',
            'monkey', 'dragon', 'master', 'sunshine', '000000', 'abc123'
        ]
    
    def analyze_password(self, password: str) -> dict:
        """
        Perform comprehensive password analysis.
        
        Args:
            password (str): Password to analyze
            
        Returns:
            dict: Analysis results including strength, entropy, and recommendations
        """
        # Get basic properties first
        has_lowercase = bool(re.search(r'[a-z]', password))
        has_uppercase = bool(re.search(r'[A-Z]', password))
        has_digits = bool(re.search(r'\d', password))
        has_symbols = bool(re.search(r'[!@#$%^&*()_\-+=\[\]{};:,.<>?/\\|`~]', password))
        is_dictionary_word = password.lower() in self.weak_passwords
        entropy = self.calculate_entropy(password)
        
        # Calculate strength WITHOUT calling analyze_password again
        strength = self._calculate_strength_internal(
            len(password), has_lowercase, has_uppercase, 
            has_digits, has_symbols, is_dictionary_word
        )
        
        # Get recommendations
        recommendations = self._get_recommendations_internal(
            len(password), has_lowercase, has_uppercase,
            has_digits, has_symbols, is_dictionary_word
        )
        
        return {
            'password_length': len(password),
            'has_lowercase': has_lowercase,
            'has_uppercase': has_uppercase,
            'has_digits': has_digits,
            'has_symbols': has_symbols,
            'entropy': entropy,
            'is_dictionary_word': is_dictionary_word,
            'strength': strength,
            'recommendations': recommendations
        }
    
    def calculate_entropy(self, password: str) -> float:
        """
        Calculate Shannon entropy of password.
        
        Entropy = log2(charset_size) * password_length
        Higher entropy = more randomness = stronger password
        
        Args:
            password (str): Password to evaluate
            
        Returns:
            float: Entropy in bits (rounded to 2 decimals)
        """
        if not password:
            return 0
        
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26  # a-z
        if any(c.isupper() for c in password):
            charset_size += 26  # A-Z
        if any(c.isdigit() for c in password):
            charset_size += 10  # 0-9
        if any(not c.isalnum() for c in password):
            charset_size += 32  # Special characters
        
        entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
        return round(entropy, 2)
    
    def _calculate_strength_internal(self, length: int, has_lower: bool, 
                                     has_upper: bool, has_digits: bool, 
                                     has_symbols: bool, is_dict_word: bool) -> str:
        """
        Internal method to calculate strength (AVOID RECURSION).
        
        Scoring:
        - Length: 1 point per 4 characters
        - Features: 10 pts each for upper, lower, digit
        - Symbols: 15 points
        - Weakness: -20 if in dictionary
        
        Args:
            length: Password length
            has_lower: Has lowercase letters
            has_upper: Has uppercase letters
            has_digits: Has digits
            has_symbols: Has symbols
            is_dict_word: Is dictionary word
            
        Returns:
            str: Strength rating (WEAK, FAIR, GOOD, STRONG)
        """
        score = 0
        
        # Calculate score
        score += length // 4
        score += 10 if has_lower else 0
        score += 10 if has_upper else 0
        score += 10 if has_digits else 0
        score += 15 if has_symbols else 0
        score -= 20 if is_dict_word else 0
        
        # Rate strength
        if score < 20:
            return 'WEAK'
        elif score < 40:
            return 'FAIR'
        elif score < 60:
            return 'GOOD'
        else:
            return 'STRONG'
    
    def _get_recommendations_internal(self, length: int, has_lower: bool,
                                      has_upper: bool, has_digits: bool,
                                      has_symbols: bool, is_dict_word: bool) -> list:
        """
        Internal method to get recommendations (AVOID RECURSION).
        
        Args:
            length: Password length
            has_lower: Has lowercase letters
            has_upper: Has uppercase letters
            has_digits: Has digits
            has_symbols: Has symbols
            is_dict_word: Is dictionary word
            
        Returns:
            list: List of recommendations
        """
        recs = []
        
        if length < 12:
            recs.append(f"Increase length to 12+ characters (currently {length})")
        if not has_upper:
            recs.append("Add uppercase letters (A-Z)")
        if not has_digits:
            recs.append("Add numbers (0-9)")
        if not has_symbols:
            recs.append("Add special characters (!@#$%^&*)")
        if is_dict_word:
            recs.append("Avoid common dictionary words")
        
        return recs if recs else ["Password meets security standards"]
    
    def calculate_strength(self, password: str) -> str:
        """Public method to calculate strength."""
        result = self.analyze_password(password)
        return result['strength']
    
    def get_recommendations(self, password: str) -> list:
        """Public method to get recommendations."""
        result = self.analyze_password(password)
        return result['recommendations']


if __name__ == '__main__':
    # Example usage
    analyzer = PasswordAnalyzer()
    test_password = "MyPassword123!"
    result = analyzer.analyze_password(test_password)
    print(f"Password: {test_password}")
    print(f"Strength: {result['strength']}")
    print(f"Entropy: {result['entropy']} bits")
