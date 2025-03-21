from src.calculator import (
    add, subtract, multiply, divide
)
import pytest

# * --------------------------------------------------------------
# * Addition Test Cases
# * --------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (2, 3, 5),
        (-1, 2, 1)
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected


# * ----------------------------
# * Subtraction Test Cases
# * ----------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 2, 3),
        (2, 5, -3),
        (0, 0, 0),
    ]
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


# * ----------------------------
# * Multiplication Test Cases
# * ----------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (0, 5, 0),
        (-2, 3, -6),
    ]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


# * ----------------------------
# * Division Test Cases
# * ----------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (5, 2, 2.5),
        (9, 3, 3),
        (5, 0, "Error! Cannot divide by zero."),
    ]
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected