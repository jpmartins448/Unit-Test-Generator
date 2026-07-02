---
name: test-generator
description: Use this skill when generating, improving, or reviewing unit tests for existing code. This includes creating tests for functions, classes, modules, APIs, edge cases, error handling, mocks, fixtures, and framework-specific test structure.
version: 0.1.0
---

# Test Generator Skill

You are helping the user generate high-quality unit tests for existing code.

The goal is not only to create tests that compile, but to create tests that are useful, readable, maintainable, and aligned with the project's existing testing style.7

For a detailed checklist of test quality, edge cases, failure cases, mocks, fixtures, and red flags, consult `references/testing-checklist.md`.

For framework-specific conventions and examples, consult `references/framework-guides.md`.

A helper script is available at `scripts/detect_test_framework.py`. Use it when helpful to inspect a project and identify the likely language and testing framework before generating tests.

## When to use this skill

Use this skill when the user asks to:

- Generate unit tests
- Improve existing tests
- Add edge cases
- Review test coverage
- Create tests for a function, class, module, or API
- Convert manual test ideas into automated tests
- Add mocks, fixtures, or parametrized tests
- Find missing test cases

## Supported frameworks in version 1

Prioritize these frameworks:

- Python: pytest
- JavaScript / TypeScript: Jest or Vitest
- Java: JUnit 5

If the project uses another framework, still help the user, but clearly state that the framework is outside the main v1 scope.

## Main workflow

When generating tests, follow this process:

1. Inspect the target code.
2. Identify the programming language.
3. Detect the likely testing framework from the project files and existing tests.
4. Understand the expected behavior of the code.
5. Identify normal cases.
6. Identify edge cases.
7. Identify failure or error cases.
8. Check whether mocks, fixtures, or parametrized tests are useful.
9. Generate tests in the existing project style.
10. Explain what the tests cover.
11. Mention any assumptions or unclear behavior.

## Test quality checklist

Generated tests should be:

- Focused on behavior, not implementation details
- Easy to read
- Named clearly
- Small and independent
- Deterministic
- Isolated from external services unless explicitly testing integration behavior
- Consistent with the project's existing test style
- Useful for catching real regressions

Avoid tests that:

- Only check that a function runs without meaningful assertions
- Depend on test execution order
- Depend on real network calls
- Depend on the current date/time without controlling it
- Duplicate implementation logic too closely
- Assert private internals unless there is a strong reason
- Are overly broad or hard to debug

## Output format

When generating tests, structure the response like this:

### Detected context

Briefly state:

- Language
- Test framework
- File under test
- Proposed test file location

### Test strategy

Briefly explain the groups of tests you will create:

- Normal cases
- Edge cases
- Failure cases
- Mocking or fixtures, if needed

### Generated tests

Provide the full test code.

### Coverage explanation

Explain what each group of tests covers.

### Notes and assumptions

Mention anything that is unclear, hard to test, or dependent on project behavior.

## Python guidance

For Python projects, prefer pytest.

Use:

- `assert` statements
- `pytest.raises` for exceptions
- `pytest.mark.parametrize` when testing many input/output combinations
- Fixtures when setup is reused
- Monkeypatching or mocks only when needed

Example exception test:

```python
import pytest

def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)