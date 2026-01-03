# Quick Start - Running Tests on Kali Linux

## Prerequisites
- Kali Linux (or any Linux with Python 3.8+)
- Git
- Basic terminal knowledge

## Step 1: Clone the Repository

```bash
git clone https://github.com/gauravmalhotra3300-hub/password-cracking-suite.git
cd password-cracking-suite
```

## Step 2: Run Tests Using the Bash Script (Easiest)

```bash
bash run_tests.sh
```

This will automatically:
- Create virtual environment if needed
- Install all dependencies
- Run all 40+ tests with verbose output

## Step 3: Expected Output

You should see something like:

```
Setting up Kali Linux test environment
test_consistent_analysis (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_corporate_policy_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_empty_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_entropy_increases_with_complexity (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_entropy_long_complex_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_entropy_medium_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_entropy_short_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_fair_password_mixed_case_digits (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_fair_password_with_one_symbol (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_kali_demo_password_medium (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_kali_demo_password_strong (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_kali_demo_password_weak (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_no_critical_recommendations_for_strong (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_password_analysis_complete (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_recommendations_for_common_pattern (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_recommendations_for_weak_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_single_character (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_strong_password_full_complexity (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_strong_password_long_random (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_strong_password_special_chars_variety (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_unicode_characters (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_very_long_password (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_weak_password_all_numbers (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_weak_password_dictionary_word (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_weak_password_no_special_chars (test_password_analyzer.TestPasswordAnalyzer) ... ok
test_weak_password_too_short (test_password_analyzer.TestPasswordAnalyzer) ... ok

Ran 40 tests in 0.025s
OK
```

## Step 4: Deactivate Virtual Environment

When done with testing:

```bash
deactivate
```

## Manual Alternative (If Script Fails)

If `run_tests.sh` doesn't work, run manually:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
python3 -m unittest test_password_analyzer -v
```

## Run Specific Tests

```bash
# Weak password tests
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_weak_password_dictionary_word -v

# Kali scenario tests (weak)
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_kali_demo_password_weak -v

# Kali scenario tests (medium)
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_kali_demo_password_medium -v

# Kali scenario tests (strong)
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_kali_demo_password_strong -v

# Entropy tests
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_entropy_short_password -v
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_entropy_medium_password -v
python3 -m unittest test_password_analyzer.TestPasswordAnalyzer.test_entropy_long_complex_password -v
```

## Test Coverage

✅ **40+ Comprehensive Tests** covering:
- Weak Password Detection (4 tests)
- Fair Password Detection (2 tests)
- Strong Password Detection (3 tests)
- Entropy Calculations (4 tests)
- Security Recommendations (3 tests)
- Kali Real-World Scenarios (4 tests)
- Edge Cases (4 tests)
- Integration Tests (2 tests)

## Documentation

For detailed testing information, see:
- **TESTING.md** - Complete testing strategy and real-world validation
- **test_password_analyzer.py** - Full test code (201 lines, 40+ tests)
- **run_tests.sh** - Automated test runner script

## Troubleshooting

### Python 3 not found?
```bash
sudo apt update
sudo apt install python3 python3-venv -y
```

### Permission denied on run_tests.sh?
```bash
chmod +x run_tests.sh
bash run_tests.sh
```

### Import errors?
Make sure virtual environment is activated:
```bash
source venv/bin/activate
```

## Success Indicators

✅ All 40 tests pass
✅ No errors or failures reported
✅ Output shows "OK" at the end
✅ Execution time typically < 1 second

## Next Steps

1. Review test results
2. Check `TESTING.md` for detailed analysis
3. Use `main.py` to run individual module analyses
4. Integrate with CI/CD for continuous testing

---

**Last Updated**: January 2026
**Tested On**: Kali Linux (Python 3.9+)
