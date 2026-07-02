# Test Generator Skill

A Claude Code Skill for generating high-quality unit tests for existing code.

This skill helps Claude Code create tests that are not only syntactically correct, but also useful, readable, and focused on real software behavior.

It supports Python, JavaScript, TypeScript, and Java projects, with first-class guidance for:

- `pytest`
- `Jest`
- `Vitest`
- `JUnit 5`

## Why this project exists

AI tools can generate tests quickly, but the generated tests are often shallow.

Common problems include:

- Testing implementation details instead of behavior
- Missing edge cases
- Missing failure cases
- Weak assertions
- Overusing mocks
- Ignoring the project's existing test style
- Creating tests that look correct but do not catch real bugs

This skill gives Claude Code a structured testing workflow so it generates better tests.

## What the skill does

When asked to generate tests, the skill guides Claude Code to:

1. Inspect the target code.
2. Identify the programming language.
3. Detect the likely testing framework.
4. Understand the expected behavior.
5. Generate normal-case tests.
6. Generate edge-case tests.
7. Generate failure-case tests.
8. Use mocks, fixtures, or parameterized tests when useful.
9. Match the existing project style.
10. Explain what the tests cover.
11. Mention unclear behavior or missing requirements.

## Repository structure

```text
test-generator-skill/
  .github/
    workflows/
      ci.yml
  skills/
    test-generator/
      SKILL.md
      examples/
        python-example.md
        javascript-example.md
        java-example.md
      references/
        testing-checklist.md
        framework-guides.md
      scripts/
        detect_test_framework.py
  tests/
    test_detect_test_framework.py
  requirements-dev.txt
  README.md
  LICENSE
```

## Skill layout

The main skill is located at:

```text
skills/test-generator/SKILL.md
```

Supporting files are included to make the skill more reliable:

```text
skills/test-generator/references/testing-checklist.md
```

Contains general testing guidance, including:

- Normal cases
- Edge cases
- Failure cases
- Side effects
- Determinism
- Independence
- Mocks
- Fixtures
- Parameterized tests
- Red flags in code under test

```text
skills/test-generator/references/framework-guides.md
```

Contains framework-specific guidance for:

- Python with pytest
- JavaScript and TypeScript with Jest
- JavaScript and TypeScript with Vitest
- Java with JUnit 5

```text
skills/test-generator/scripts/detect_test_framework.py
```

A small dependency-free Python helper script that detects the likely test framework used by a project.

## Example usage

Inside Claude Code, a user can ask:

```text
Use the test-generator skill to generate unit tests for this function.
Include normal cases, edge cases, and failure cases.
```

Or:

```text
Use the test-generator skill to review the existing tests for this module and suggest missing cases.
```

Or:

```text
Use the test-generator skill to generate pytest tests for this Python file.
```

## Example output

For this Python function:

```python
def divide(a, b):
    return a / b
```

The skill should guide Claude Code to generate tests like:

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

And explain that the tests cover:

- Normal division
- Negative numbers
- Zero as numerator
- Floating-point inputs
- Division by zero

## Framework detector script

The project includes a helper script that tries to detect the likely test framework used by a repository.

Run it with:

```bash
python skills/test-generator/scripts/detect_test_framework.py .
```

Example output:

```json
{
  "language": "python",
  "framework": "pytest",
  "confidence": "high",
  "evidence": [
    "pyproject.toml contains 'pytest'"
  ]
}
```

The script currently checks common project files such as:

- `package.json`
- `pyproject.toml`
- `requirements.txt`
- `requirements-dev.txt`
- `setup.cfg`
- `tox.ini`
- `pom.xml`
- `build.gradle`
- `build.gradle.kts`

## Supported frameworks

| Language | Framework | Status |
|---|---|---|
| Python | pytest | Supported |
| Python | unittest | Detection only |
| JavaScript | Jest | Supported |
| TypeScript | Jest | Supported |
| JavaScript | Vitest | Supported |
| TypeScript | Vitest | Supported |
| Java | JUnit 5 | Supported |

## Running tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the test suite:

```bash
python -m pytest
```

Expected result:

```text
11 passed
```

## Continuous integration

This repository includes a GitHub Actions workflow:

```text
.github/workflows/ci.yml
```

The workflow runs automatically on:

- Pushes to `main`
- Pushes to `master`
- Pull requests

It installs development dependencies and runs:

```bash
python -m pytest
```

## Example files

The `examples/` folder contains sample inputs and expected test outputs:

```text
skills/test-generator/examples/python-example.md
skills/test-generator/examples/javascript-example.md
skills/test-generator/examples/java-example.md
```

These examples show how the skill should behave for different languages and frameworks.

## Design goals

This project is intentionally small, readable, and beginner-friendly.

The goal is not to build a huge testing platform.

The goal is to show:

- Practical understanding of unit testing
- AI-assisted developer tooling
- Good documentation
- Basic static analysis
- Automated testing
- GitHub Actions CI
- Clean project structure

## Roadmap

Possible future improvements:

- Add support for Go testing
- Add support for C# and xUnit
- Add support for React Testing Library
- Add support for Python FastAPI route tests
- Add support for Spring Boot service tests
- Improve framework detection with more project files
- Add confidence scoring across multiple detected frameworks
- Add a CLI option for machine-readable output
- Add example demo videos or screenshots
- Add more real-world examples
- Add test quality scoring
- Add mutation-testing recommendations

## Limitations

This skill does not automatically guarantee that generated tests are correct.

Generated tests should still be reviewed by a developer.

The framework detector is intentionally simple and may not detect every project setup.

The skill focuses on unit tests, not full end-to-end or performance tests.

## License

MIT License.