"""Simple calculator module with intentional bugs for testing."""


class Calculator:
    """A basic calculator class."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def modulo(self, a, b):
        """Return the remainder of a divided by b.

        BUG: Does not handle modulo by zero!
        """
        return a % b
