"""Tests for the Calculator module."""

import pytest
from src.calculator import Calculator


@pytest.fixture
def calculator():
    """Create a Calculator instance for testing."""
    return Calculator()


class TestAdd:
    """Test cases for the add method."""

    def test_add_positive_numbers(self, calculator):
        assert calculator.add(2, 3) == 5

    def test_add_negative_numbers(self, calculator):
        assert calculator.add(-1, -1) == -2

    def test_add_zero(self, calculator):
        assert calculator.add(5, 0) == 5


class TestSubtract:
    """Test cases for the subtract method."""

    def test_subtract_positive(self, calculator):
        assert calculator.subtract(5, 3) == 2

    def test_subtract_negative_result(self, calculator):
        assert calculator.subtract(3, 5) == -2


class TestMultiply:
    """Test cases for the multiply method."""

    def test_multiply_positive(self, calculator):
        assert calculator.multiply(3, 4) == 12

    def test_multiply_by_zero(self, calculator):
        assert calculator.multiply(5, 0) == 0

    def test_multiply_negative(self, calculator):
        assert calculator.multiply(-2, 3) == -6


class TestDivide:
    """Test cases for the divide method."""

    def test_divide_evenly(self, calculator):
        assert calculator.divide(10, 2) == 5.0

    def test_divide_with_remainder(self, calculator):
        assert calculator.divide(7, 2) == 3.5

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)
