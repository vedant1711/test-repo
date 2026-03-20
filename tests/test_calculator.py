"""Tests for the calculator module."""
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """This test SHOULD pass but will FAIL because divide doesn't handle zero."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        assert self.calc.modulo(10, 3) == 1
