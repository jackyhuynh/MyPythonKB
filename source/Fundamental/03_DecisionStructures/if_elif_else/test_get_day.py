"""
Unit test for all the get day
"""
import unittest

from if_elif_else import get_day_if_elif_else
from if_else_if import get_day_if_else_if


# pylint: disable=duplicate-code
class TestDayOfWeek(unittest.TestCase):
    """
    Test cases for the get_day_if_else_if and get_day_if_elif_else functions.
    """

    def test_get_day_if_else_if(self):
        """
        Test the get_day_if_else_if function with valid and invalid inputs.
        """
        self.assertEqual(get_day_if_else_if(1), "Monday")
        self.assertEqual(get_day_if_else_if(2), "Tuesday")
        self.assertEqual(get_day_if_else_if(3), "Wednesday")
        self.assertEqual(get_day_if_else_if(4), "Thursday")
        self.assertEqual(get_day_if_else_if(5), "Friday")
        self.assertEqual(get_day_if_else_if(6), "Saturday")
        self.assertEqual(get_day_if_else_if(7), "Sunday")
        self.assertEqual(get_day_if_else_if(8),
                         "Error: "
                         "Invalid number, please enter a number between 1 and 7.")
        self.assertEqual(get_day_if_else_if(0),
                         "Error: "
                         "Invalid number, please enter a number between 1 and 7.")

    def test_get_day_if_elif_else(self):
        """
        Test the get_day_if_elif_else function with valid and invalid inputs.
        """
        self.assertEqual(get_day_if_elif_else(1), "Monday")
        self.assertEqual(get_day_if_elif_else(2), "Tuesday")
        self.assertEqual(get_day_if_elif_else(3), "Wednesday")
        self.assertEqual(get_day_if_elif_else(4), "Thursday")
        self.assertEqual(get_day_if_elif_else(5), "Friday")
        self.assertEqual(get_day_if_elif_else(6), "Saturday")
        self.assertEqual(get_day_if_elif_else(7), "Sunday")
        self.assertEqual(get_day_if_elif_else(8),
                         "Error: "
                         "Invalid number, please enter a number between 1 and 7.")
        self.assertEqual(get_day_if_elif_else(0),
                         "Error: "
                         "Invalid number, please enter a number between 1 and 7.")


if __name__ == "__main__":
    unittest.main()
