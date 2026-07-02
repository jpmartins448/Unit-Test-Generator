import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sample-input-code"))

from calculator import divide, format_username, is_even


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (-10, 2, -5),
        (0, 5, 0),
        (7.5, 2.5, 3),
    ],
)
def test_divide_valid_inputs(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize(
    "number,expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-5, False),
    ],
)
def test_is_even(number, expected):
    assert is_even(number) is expected


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice Smith", "alice_smith"),
        ("  Alice Smith  ", "alice_smith"),
        ("JOHN", "john"),
        ("Mary Jane Watson", "mary_jane_watson"),
    ],
)
def test_format_username(name, expected):
    assert format_username(name) == expected


def test_format_username_empty_string():
    assert format_username("") == ""