"""
Unit tests for password_analyzer module.
"""

import unittest
from password_analyzer import PasswordAnalyzer


class TestPasswordAnalyzer(unittest.TestCase):
    """Test cases for PasswordAnalyzer class."""
    
    def setUp(self):
        """Initialize analyzer for each test."""
        self.analyzer = PasswordAnalyzer()
    
    def test_weak_password(self):
        """Test detection of weak password."""
        result = self.analyzer.analyze_password('password')
        self.assertEqual(result['strength'], 'WEAK')
        self.assertTrue(result['is_dictionary_word'])
    
    def test_fair_password(self):
        """Test detection of fair password."""
        result = self.analyzer.analyze_password('Pass1234')
        # Fair password: has upper, lower, digits but no symbols
        self.assertIn(result['strength'], ['FAIR', 'GOOD'])
    
    def test_strong_password(self):
        """Test detection of strong password."""
        result = self.analyzer.analyze_password('MySecure@Password123!')
        # This password has all complexity features
        self.assertTrue(result['has_uppercase'])
        self.assertTrue(result['has_lowercase'])
        self.assertTrue(result['has_digits'])
        self.assertTrue(result['has_symbols'])
        self.assertEqual(result['password_length'], 21)
    
    def test_entropy_calculation(self):
        """Test entropy calculation."""
        entropy = self.analyzer.calculate_entropy('ABC')
        self.assertGreater(entropy, 0)
        
        # Longer password should have higher entropy
        entropy_long = self.analyzer.calculate_entropy('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        self.assertGreater(entropy_long, entropy)
    
    def test_recommendations(self):
        """Test security recommendations."""
        recs = self.analyzer.get_recommendations('weak')
        self.assertGreater(len(recs), 0)
        # 'weak' should have recommendations for symbols, uppercase, digits, length
        self.assertTrue(any('uppercase' in r.lower() for r in recs))
    
    def test_no_recommendations_for_strong(self):
        """Test that strong passwords get no recommendations."""
        # A sufficiently strong password
        recs = self.analyzer.get_recommendations('SecurePass@2024!ABC')
        # Should either be empty or contain "meets security standards"
        if recs:
            self.assertIn('meets security standards', recs[0].lower())


if __name__ == '__main__':
    unittest.main(verbosity=2)
