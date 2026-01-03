"""
Comprehensive unit tests for password_analyzer module.
Includes Kali Linux testing scenarios for real-world validation.
"""
import unittest
from password_analyzer import PasswordAnalyzer


class TestPasswordAnalyzer(unittest.TestCase):
    """Test cases for PasswordAnalyzer class with real-world scenarios."""

    def setUp(self):
        """Initialize analyzer for each test."""
        self.analyzer = PasswordAnalyzer()

    # ==================== WEAK PASSWORD TESTS ====================
    def test_weak_password_dictionary_word(self):
        """Test detection of weak password (common dictionary word)."""
        result = self.analyzer.analyze_password('password')
        self.assertEqual(result['strength'], 'WEAK')
        self.assertTrue(result['is_dictionary_word'])

    def test_weak_password_too_short(self):
        """Test detection of weak password (too short)."""
        result = self.analyzer.analyze_password('Pass1')
        self.assertIn(result['strength'], ['WEAK', 'FAIR'])
        self.assertLess(result['password_length'], 8)

    def test_weak_password_no_special_chars(self):
        """Test weak password without special characters."""
        result = self.analyzer.analyze_password('Password123')
        self.assertFalse(result['has_symbols'])

    def test_weak_password_all_numbers(self):
        """Test detection of all-numeric password."""
        result = self.analyzer.analyze_password('12345678')
        self.assertEqual(result['strength'], 'WEAK')
        self.assertTrue(result['has_digits'])
        self.assertFalse(result['has_uppercase'])
        self.assertFalse(result['has_lowercase'])

    # ==================== FAIR PASSWORD TESTS ====================
    def test_fair_password_mixed_case_digits(self):
        """Test detection of fair password with mixed case and digits."""
        result = self.analyzer.analyze_password('Pass1234')
        self.assertIn(result['strength'], ['FAIR', 'GOOD'])
        self.assertTrue(result['has_uppercase'])
        self.assertTrue(result['has_lowercase'])
        self.assertTrue(result['has_digits'])
        self.assertFalse(result['has_symbols'])

    def test_fair_password_with_one_symbol(self):
        """Test fair password with single symbol."""
        result = self.analyzer.analyze_password('Pass123@')
        self.assertIn(result['strength'], ['FAIR', 'GOOD'])
        self.assertTrue(result['has_symbols'])

    # ==================== STRONG PASSWORD TESTS ====================
    def test_strong_password_full_complexity(self):
        """Test detection of strong password with all features."""
        result = self.analyzer.analyze_password('MySecure@Password123!')
        self.assertTrue(result['has_uppercase'])
        self.assertTrue(result['has_lowercase'])
        self.assertTrue(result['has_digits'])
        self.assertTrue(result['has_symbols'])
        self.assertEqual(result['password_length'], 21)

    def test_strong_password_long_random(self):
        """Test detection of long random password."""
        result = self.analyzer.analyze_password('Xy7!kL90#Qw9Rt2@Zx5')
        self.assertIn(result['strength'], ['STRONG', 'GOOD'])
        self.assertGreater(result['password_length'], 15)

    def test_strong_password_special_chars_variety(self):
        """Test password with multiple special characters."""
        result = self.analyzer.analyze_password('P@ssW0rd!#$%^&')
        self.assertTrue(result['has_symbols'])
        self.assertGreater(result['entropy'], 50)  # High entropy

    # ==================== ENTROPY CALCULATION TESTS ====================
    def test_entropy_short_password(self):
        """Test entropy calculation for short password."""
        entropy = self.analyzer.calculate_entropy('ABC')
        self.assertGreater(entropy, 0)
        self.assertLess(entropy, 20)  # Short password = low entropy

    def test_entropy_medium_password(self):
        """Test entropy calculation for medium password."""
        entropy = self.analyzer.calculate_entropy('Password123')
        self.assertGreater(entropy, 30)
        self.assertLess(entropy, 70)

    def test_entropy_long_complex_password(self):
        """Test entropy for long complex password."""
        entropy_short = self.analyzer.calculate_entropy('ABC')
        entropy_long = self.analyzer.calculate_entropy('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$')
        self.assertGreater(entropy_long, entropy_short)
        self.assertGreater(entropy_long, 100)

    def test_entropy_increases_with_complexity(self):
        """Test that entropy increases with password complexity."""
        entropy_simple = self.analyzer.calculate_entropy('password')
        entropy_complex = self.analyzer.calculate_entropy('P@ssw0rd!2024')
        self.assertGreater(entropy_complex, entropy_simple)

    # ==================== RECOMMENDATIONS TESTS ====================
    def test_recommendations_for_weak_password(self):
        """Test security recommendations for weak passwords."""
        recs = self.analyzer.get_recommendations('weak')
        self.assertGreater(len(recs), 0)
        self.assertTrue(any('uppercase' in r.lower() for r in recs))

    def test_recommendations_for_common_pattern(self):
        """Test recommendations for passwords with common patterns."""
        recs = self.analyzer.get_recommendations('password')
        self.assertGreater(len(recs), 0)
        # Should recommend avoiding dictionary words
        self.assertTrue(any('dictionary' in r.lower() or 'common' in r.lower() for r in recs))

    def test_no_critical_recommendations_for_strong(self):
        """Test that strong passwords get minimal recommendations."""
        recs = self.analyzer.get_recommendations('SecurePass@2024!ABC')
        if recs:
            # If there are recs, they should be positive
            self.assertIn('meets security standards', recs[0].lower())

    # ==================== REAL-WORLD SCENARIO TESTS ====================
    def test_corporate_policy_password(self):
        """Test password following common corporate 8-char policy.
        Policy: Minimum 8 chars, 1 uppercase, 1 lowercase, 1 digit.
        """
        password = 'Welcome1'
        result = self.analyzer.analyze_password(password)
        self.assertEqual(result['password_length'], 8)
        self.assertTrue(result['has_uppercase'])
        self.assertTrue(result['has_lowercase'])
        self.assertTrue(result['has_digits'])

    def test_kali_demo_password_weak(self):
        """Test weak demo password from Kali test scenario."""
        result = self.analyzer.analyze_password('Admin@123')
        self.assertEqual(result['strength'], 'WEAK')
        # Common pattern with predictable numbers

    def test_kali_demo_password_medium(self):
        """Test medium strength password from Kali scenario."""
        result = self.analyzer.analyze_password('Welcome2024')
        self.assertIn(result['strength'], ['FAIR', 'GOOD'])

    def test_kali_demo_password_strong(self):
        """Test strong password from Kali scenario."""
        result = self.analyzer.analyze_password('Xy7!kL90#Qw')
        self.assertIn(result['strength'], ['STRONG', 'GOOD'])

    # ==================== EDGE CASE TESTS ====================
    def test_empty_password(self):
        """Test handling of empty password."""
        result = self.analyzer.analyze_password('')
        self.assertEqual(result['strength'], 'WEAK')
        self.assertEqual(result['password_length'], 0)

    def test_single_character(self):
        """Test single character password."""
        result = self.analyzer.analyze_password('a')
        self.assertEqual(result['strength'], 'WEAK')

    def test_unicode_characters(self):
        """Test password with unicode characters."""
        result = self.analyzer.analyze_password('P@ssw0rdéèê')
        self.assertGreater(result['password_length'], 8)

    def test_very_long_password(self):
        """Test very long password (100+ characters)."""
        long_pwd = 'a' * 100 + 'A' + '1' + '!'
        result = self.analyzer.analyze_password(long_pwd)
        self.assertEqual(result['password_length'], 104)
        self.assertGreater(result['entropy'], 100)

    # ==================== INTEGRATION TESTS ====================
    def test_password_analysis_complete(self):
        """Integration test: analyze password returns all required fields."""
        result = self.analyzer.analyze_password('Test@1234')
        required_fields = [
            'strength', 'password_length', 'entropy',
            'has_uppercase', 'has_lowercase', 'has_digits', 'has_symbols',
            'is_dictionary_word'
        ]
        for field in required_fields:
            self.assertIn(field, result, f"Missing field: {field}")

    def test_consistent_analysis(self):
        """Test that same password always produces same analysis."""
        pwd = 'MyPassword@2024'
        result1 = self.analyzer.analyze_password(pwd)
        result2 = self.analyzer.analyze_password(pwd)
        self.assertEqual(result1['entropy'], result2['entropy'])
        self.assertEqual(result1['strength'], result2['strength'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
