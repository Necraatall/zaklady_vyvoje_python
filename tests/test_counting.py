"""
Test Suite pro module counting.py
"""

import unittest
from parameterized import parameterized
import counting


class TestCount(unittest.TestCase):
    def setUp(self) -> None:
        """ co pred testem se ma udelat

        Returns:
            _type_: vola jen sebe a nic nevraci
        """
        print("Volani setupu")
        return super().setUp()
  
    def tearDown(self) -> None:
        """ co po testu, uklid dat

        Returns:
            _type_: vola jen sebe nic nevraci
        """
        print("Volani Teardovnu")
        return super().tearDown()
    
    @parameterized.expand([
        (1, 1, 1),
        (2, 25, 50),
        (6, 6, 36),
    ])

    def test_multiply(self, number_one, number_two, expected):
        """Testovani multiply
        """
        actual = counting.multiply(number_one, number_two)

        self.assertEqual(expected, actual)

    @parameterized.expand([
        (1, 1, 0),
        (2, 25, 40),
        (6, 6, 360),
    ])

    def test_multiply_fail(self, number_one, number_two, expected):
        """Testovani multiply
        """
        actual = counting.multiply(number_one, number_two)

        self.assertNotEqual(expected, actual)

