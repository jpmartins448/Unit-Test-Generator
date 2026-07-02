# Python Example: pytest

This example shows how the `test-generator` skill should generate pytest tests for a simple Python function.

## Input code

File: `calculator.py`

```python
def divide(a, b):
    return a / b
```

## User request

```text
Use the test-generator skill to generate unit tests for calculator.py.
Include normal cases, edge cases, and failure cases.
```

## Expected output

File: `tests/test_calculator.py`

```python
import pytest

from calculator import divide


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
```

## Coverage explanation

These tests cover:

- Normal division with positive numbers
- Negative number handling
- Zero as the numerator
- Float division
- Division by zero as a failure case

## Notes

The function does not validate input types. If the production code should reject non-numeric inputs with a custom error, additional tests should be added.