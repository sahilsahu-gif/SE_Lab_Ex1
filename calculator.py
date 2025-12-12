"""Small arithmetic utilities.

This module provides a lightweight Calculator class and a couple of
module-level helper functions for simple arithmetic. It validates inputs
and keeps a small, well-named public API that is easy to test and reuse.
"""

from __future__ import annotations
from typing import Union

Number = Union[int, float]


def _ensure_number(value: object, name: str) -> Number:
    """Validate a single value is an int or float and return it.

    Raises:
        TypeError: if the value is not int or float.
    """
    if isinstance(value, (int, float)):
        return value
    raise TypeError(f"{name!r} must be an int or float, got {type(value).__name__!r}.")


def add_numbers(a: object, b: object) -> Number:
    """Return the sum of a and b after validating inputs."""
    a_val = _ensure_number(a, "a")
    b_val = _ensure_number(b, "b")
    return a_val + b_val


def subtract_numbers(a: object, b: object) -> Number:
    """Return the difference (a - b) after validating inputs."""
    a_val = _ensure_number(a, "a")
    b_val = _ensure_number(b, "b")
    return a_val - b_val


class Calculator:
    """A small state-less calculator exposing common arithmetic operations.

    This class is intentionally lightweight (no stored state) and simply groups
    related operations for clearer call-sites. Use module-level functions for
    convenience or this class when a namespaced API is preferred.
    """

    @staticmethod
    def add(a: object, b: object) -> Number:
        """Add two numbers."""
        return add_numbers(a, b)

    @staticmethod
    def subtract(a: object, b: object) -> Number:
        """Subtract two numbers (a - b)."""
        return subtract_numbers(a, b)


# Backwards-compatibility aliases used by tests or older code
add = add_numbers
subtract = subtract_numbers
