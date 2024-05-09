import sys
import os
from contextlib import contextmanager

@contextmanager
def extend_sys_path(path):
    """Context manager to temporarily extend sys.path with the specified directory."""
    old_sys_path = sys.path[:]
    sys.path.insert(0, path)
    try:
        yield
    finally:
        sys.path = old_sys_path

# Use the context manager to add the parent directory
with extend_sys_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))):
    from simple_calculator import SimpleCalculator  # Import the module inside the context


from simple_calculator import SimpleCalculator  # Import the module

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