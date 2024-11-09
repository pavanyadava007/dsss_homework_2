import unittest
from unittest.mock import patch
from math_quiz import generate_problem,get_random_int,get_random_operator,math_quiz

# Assume that the original code is imported or in the same file
# If the math quiz code is in a module named `math_quiz_game.py`, you would import it as follows:
# from math_quiz_game import get_random_int, get_random_operator, generate_problem, math_quiz


class TestMathQuiz(unittest.TestCase):

    # Test the get_random_int function
    def test_get_random_int(self):
        # Test that the random integer is within the specified range
        result = get_random_int(1, 10)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

        result = get_random_int(5, 15)
        self.assertGreaterEqual(result, 5)
        self.assertLessEqual(result, 15)

    # Test the get_random_operator function
    def test_get_random_operator(self):
        # Test that the random operator is one of '+', '-', or '*'
        operator = get_random_operator()
        self.assertIn(operator, ['+', '-', '*'])

    # Test the generate_problem function for correct math problems
    def test_generate_problem(self):
        # Test addition
        problem, answer = generate_problem(3, 2, '+')
        self.assertEqual(problem, "3 + 2")
        self.assertEqual(answer, 5)

        # Test subtraction
        problem, answer = generate_problem(10, 3, '-')
        self.assertEqual(problem, "10 - 3")
        self.assertEqual(answer, 7)

        # Test multiplication
        problem, answer = generate_problem(4, 5, '*')
        self.assertEqual(problem, "4 * 5")
        self.assertEqual(answer, 20)

    # Test math_quiz function
    @patch('builtins.input', side_effect=['5', '7', '8', '10', '2'])  # Mock user input
    def test_math_quiz(self, mock_input):
        # Patch the random functions to return predictable results for testing
        with patch('random.randint', side_effect=[3, 2, 10, 3, 4, 5, 4, 5, 7, 8]), \
             patch('random.choice', side_effect=['+', '-', '*', '+', '-']):

            with patch('builtins.print') as mock_print:  # Mock print to prevent actual output
                math_quiz()

                # Check if the correct score is calculated based on the mocked input
                mock_print.assert_any_call("Correct! You earned a point.")
                mock_print.assert_any_call("Game over! Your score is: 2/5")

                # Verify that the quiz runs for 5 questions
                self.assertEqual(mock_print.call_count, 15)  # print should be called multiple times

if __name__ == '__main__':
    unittest.main()
