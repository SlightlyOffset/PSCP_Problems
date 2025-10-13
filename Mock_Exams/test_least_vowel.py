import unittest
from unittest.mock import patch
import io
import sys

# Import the functions from the script we want to test
from Least_vowel import text_filtering, has_one_vowel, main

class TestLeastVowel(unittest.TestCase):
    '''Unit tests for Least_vowel.py'''

    # --- Tests for has_one_vowel ---

    def test_has_one_vowel_true(self):
        '''Test words that correctly have one vowel'''
        self.assertTrue(has_one_vowel("cat"))
        self.assertTrue(has_one_vowel("Dog")) # Case-insensitivity
        self.assertTrue(has_one_vowel("I"))

    def test_has_one_vowel_false(self):
        '''Test words that do not have exactly one vowel'''
        self.assertFalse(has_one_vowel("beautiful")) # Multiple vowels
        self.assertFalse(has_one_vowel("rhythm"))    # No vowels
        self.assertFalse(has_one_vowel(""))          # Empty string

    # --- Tests for text_filtering ---

    def test_text_filtering_with_noise(self):
        '''Test filtering of numbers and special characters'''
        self.assertEqual(text_filtering("H3llo, w0rld!"), "Hllo wrld")
        self.assertEqual(text_filtering("This is a t3st."), "This is a tst")

    def test_text_filtering_preserves_space(self):
        '''Test that whitespace is preserved'''
        self.assertEqual(text_filtering("  leading and trailing  "), "  leading and trailing  ")

    def test_text_filtering_only_noise(self):
        '''Test a string containing only noise'''
        self.assertEqual(text_filtering("123!@#$%^&*()"), "")

    def test_text_filtering_empty_string(self):
        '''Test an empty input string'''
        self.assertEqual(text_filtering(""), "")

    # --- Integration test for main() ---

    def run_main_with_input(self, input_string):
        '''Helper function to run main() with mocked input and capture output'''
        # Mock 'input' to return our test string
        with patch('builtins.input', return_value=input_string):
            # Redirect stdout to capture the print output
            with io.StringIO() as captured_output:
                sys.stdout = captured_output
                main()
                # Restore stdout
                sys.stdout = sys.__stdout__
                return captured_output.getvalue().strip()

    def test_main_function_normal_case(self):
        '''Test the main function with a typical sentence'''
        input_str = "A quick brown f0x jumps ov3r the lazy dog."
        expected_output = "A fox the dog"
        self.assertEqual(self.run_main_with_input(input_str), expected_output)

    def test_main_function_no_matching_words(self):
        '''Test the main function when no words match the criteria'''
        input_str = "Rhythm fly beautiful."
        expected_output = ""
        self.assertEqual(self.run_main_with_input(input_str), expected_output)

    def test_main_function_empty_input(self):
        '''Test the main function with an empty string input'''
        input_str = ""
        expected_output = ""
        self.assertEqual(self.run_main_with_input(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()
