import unittest
from CaesarV2 import find_decryption, shifting


class TestCaesarV2(unittest.TestCase):
    '''Unit tests for CaesarV2.py'''

    # --- Tests for shifting() ---

    def test_shifting_positive_shift_lowercase(self):
        '''Test shifting with a positive shift on lowercase letters.'''
        self.assertEqual(shifting("abc", 1), "bcd")

    def test_shifting_positive_shift_uppercase(self):
        '''Test shifting with a positive shift on uppercase letters.'''
        self.assertEqual(shifting("ABC", 3), "DEF")

    def test_shifting_positive_shift_wrapping(self):
        '''Test shifting with wrapping around the alphabet.'''
        self.assertEqual(shifting("xyz", 3), "abc")
        self.assertEqual(shifting("XYZ", 3), "ABC")

    def test_shifting_negative_shift(self):
        '''Test shifting with a negative shift.'''
        self.assertEqual(shifting("bcd", -1), "abc")
        self.assertEqual(shifting("DEF", -3), "ABC")

    def test_shifting_negative_shift_wrapping(self):
        '''Test shifting with a negative shift and wrapping.'''
        self.assertEqual(shifting("abc", -1), "zab")
        self.assertEqual(shifting("ABC", -1), "ZAB")

    def test_shifting_zero_shift(self):
        '''Test shifting with a zero shift.'''
        self.assertEqual(shifting("Hello, World!", 0), "Hello, World!")

    def test_shifting_with_punctuation_and_numbers(self):
        '''Test shifting on a message with mixed content.'''
        self.assertEqual(shifting("Hello, World! 123", 13), "Uryyb, Jbeyq! 123")

    def test_shifting_empty_string(self):
        '''Test shifting an empty string.'''
        self.assertEqual(shifting("", 10), "")

    def test_shifting_large_positive_shift(self):
        '''Test that large shifts are handled correctly via modulo.'''
        self.assertEqual(shifting("abc", 27), "bcd")

    def test_shifting_large_negative_shift(self):
        '''Test that large negative shifts are handled correctly.'''
        self.assertEqual(shifting("abc", -27), "zab")

    # --- Tests for find_decryption() ---

    def setUp(self):
        '''Set up common words for decryption tests.'''
        self.common_words = {
            "what", "when", "why", "which", "this", "there", "where",
            "the", "is", "am", "are", "you", "we", "they", "he", "she",
            "it"
        }

    def test_find_decryption_success(self):
        '''Test finding a valid decryption.'''
        encrypted = "Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph"  # shift = 1
        decrypted = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(find_decryption(encrypted, self.common_words), decrypted)

    def test_find_decryption_fail(self):
        '''Test a message that cannot be decrypted to a common word.'''
        encrypted = "qwer tyui asdf"
        self.assertIsNone(find_decryption(encrypted, self.common_words))

    def test_find_decryption_case_insensitivity(self):
        '''Test that decryption works regardless of original case.'''
        encrypted = "UIF"  # "THE" shifted by 1
        decrypted = "THE"
        self.assertEqual(find_decryption(encrypted, self.common_words), decrypted)

    def test_find_decryption_with_punctuation(self):
        '''Test decryption of a message with punctuation.'''
        encrypted = "Nx ymnx ny?"  # "Is this it?" shifted by 5
        decrypted = "Is this it?"
        self.assertEqual(find_decryption(encrypted, self.common_words), decrypted)


if __name__ == '__main__':
    unittest.main()
