# Demo

This folder shows a simple example of how the `test-generator` skill should behave.

## Input

The file `sample-input-code/calculator.py` contains three small Python functions:

- `divide`
- `is_even`
- `format_username`

## Expected generated tests

The file `sample-output-tests/test_calculator.py` shows the type of pytest tests the skill should generate.

The tests include:

- Normal cases
- Edge cases
- Failure cases
- Parameterized tests
- Clear test names

## Example prompt

```text
Use the test-generator skill to generate pytest tests for demo/sample-input-code/calculator.py.
Include normal cases, edge cases, and failure cases.