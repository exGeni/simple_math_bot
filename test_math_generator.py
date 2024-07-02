import unittest
from math_generator import generate_addition, generate_subtraction, generate_multiplication, generate_division

class TestMathGenerator(unittest.TestCase):
    """
    Test suite for the math example generator functions.
    This class contains test methods for each type of mathematical operation.
    """

    def test_generate_addition(self):
        """
        Test the addition example generator.
        Checks if the generated example is a string and contains the correct symbols.
        """
        for level in [1, 2, 3]:
            result = generate_addition(level)
            self.assertIsInstance(result, str, f"Result should be a string for level {level}")
            self.assertIn('➕', result, f"Addition symbol not found in result for level {level}")
            self.assertIn('🟰', result, f"Equals symbol not found in result for level {level}")

    def test_generate_subtraction(self):
        """
        Test the subtraction example generator.
        Checks if the generated example is a string and contains the correct symbols.
        """
        for level in [1, 2, 3]:
            result = generate_subtraction(level)
            self.assertIsInstance(result, str, f"Result should be a string for level {level}")
            self.assertIn('➖', result, f"Subtraction symbol not found in result for level {level}")
            self.assertIn('🟰', result, f"Equals symbol not found in result for level {level}")

    def test_generate_multiplication(self):
        """
        Test the multiplication example generator.
        Checks if the generated example is a string and contains the correct symbols.
        For level 3, it also checks for power symbols as an alternative to multiplication.
        """
        for level in [1, 2]:
            result = generate_multiplication(level)
            self.assertIsInstance(result, str, f"Result should be a string for level {level}")
            self.assertIn('✖️', result, f"Multiplication symbol not found in result for level {level}")
            self.assertIn('🟰', result, f"Equals symbol not found in result for level {level}")
        
        # Separate test for level 3
        result = generate_multiplication(3)
        self.assertIsInstance(result, str, "Result should be a string for level 3")
        self.assertIn('🟰', result, "Equals symbol not found in result for level 3")
        # Check that the result contains either multiplication or a power symbol
        self.assertTrue('✖️' in result or any(power in result for power in ['²', '³', '⁴', '⁵']), 
                        "Neither multiplication nor power symbol found in result for level 3")

    def test_generate_division(self):
        """
        Test the division example generator.
        Checks if the generated example is a string and contains the correct symbols.
        """
        for level in [1, 2, 3]:
            result = generate_division(level)
            self.assertIsInstance(result, str, f"Result should be a string for level {level}")
            self.assertIn('➗', result, f"Division symbol not found in result for level {level}")
            self.assertIn('🟰', result, f"Equals symbol not found in result for level {level}")

if __name__ == '__main__':
    unittest.main()