import unittest
from source.anagram import anagram


class TestAnagram(unittest.TestCase):
    def test_two_strings_are_angram(self):
        """
        Test two strings are anagram 
        """
        str1 = "Testtwostringsareanagram"
        str2 = "areanagramTesttwostrings"
        result = anagram(str1, str2)
        self.assertTrue(result)

    def test_two_strings_are_not_angram(self):
        """
        Test two strings are not anagram 
        """
        str1 = "armyone"
        str2 = "Mary"
        result = anagram(str1, str2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
