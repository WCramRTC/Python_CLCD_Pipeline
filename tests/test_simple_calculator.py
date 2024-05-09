import sys
import os

# Adjust the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.simple_calculator import SimpleCalculator  # Import the module

def test_simple_calculator_add_test():

    # Arrange
    testCalculator = SimpleCalculator()
    number1 = 5
    number2 = 10
    expectedResult = 15

    # Act 
    result = testCalculator.add(number1, number2)

    # Assert
    assert result == expectedResult

def test_simple_calculator_subtract_test():

    # Arrange
    testCalculator = SimpleCalculator()
    number1 = 5
    number2 = 10
    expectedResult = -5

    # Act
    result = testCalculator.subtract(number1, number2)

    # Assert
    assert result == expectedResult