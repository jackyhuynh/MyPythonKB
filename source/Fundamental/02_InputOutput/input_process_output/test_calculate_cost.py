"""
Unit tests for the calculate_costs function from the input_processing_output module.
"""
import unittest

from input_processing_output import calculate_costs


class TestCostCalculations(unittest.TestCase):
    """
   Test cases for the calculate_costs function.
   """

    def test_calculate_costs(self):
        """
        Test the calculate_costs function with different sets of inputs.
        """
        # Test case 1
        hamburger_cost = 10
        fries_cost = 5
        shake_cost = 3
        total_cost, average_cost = calculate_costs(hamburger_cost, fries_cost, shake_cost)
        self.assertEqual(total_cost, 18)
        self.assertEqual(average_cost, 6)

        # Test case 2
        hamburger_cost = 15
        fries_cost = 10
        shake_cost = 5
        total_cost, average_cost = calculate_costs(hamburger_cost, fries_cost, shake_cost)
        self.assertEqual(total_cost, 30)
        self.assertEqual(average_cost, 10)

        # Test case 3
        hamburger_cost = 20
        fries_cost = 10
        shake_cost = 5
        total_cost, average_cost = calculate_costs(hamburger_cost, fries_cost, shake_cost)
        self.assertEqual(total_cost, 35)
        self.assertEqual(average_cost, 35 / 3)


if __name__ == '__main__':
    unittest.main()
