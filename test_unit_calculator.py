import unittest
from io import StringIO
from unittest.mock import patch
from source.calculator import calculate


class MyTestCase(unittest.TestCase):
    def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            calculate()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def testTwenty(self):
        self.runTest(20, '10 + 10')

    def testOne(self):
        self.runTest(1, '3 - 1')


if __name__ == '__main__':
    unittest.main()
