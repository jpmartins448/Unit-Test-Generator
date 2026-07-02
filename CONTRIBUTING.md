# Contributing

Thank you for your interest in contributing to Test Generator Skill.

This project is intentionally small and beginner-friendly. The goal is to improve how Claude Code generates useful unit tests for real codebases.

## Project goals

This project aims to help Claude Code generate tests that are:

- Useful
- Readable
- Deterministic
- Focused on behavior
- Consistent with the existing project style
- Clear about assumptions and limitations

## Current scope

Version 1 focuses on:

- Python with pytest
- JavaScript and TypeScript with Jest
- JavaScript and TypeScript with Vitest
- Java with JUnit 5

Support for other languages and frameworks can be added later.

## Good contribution ideas

Useful contributions include:

- Adding more examples
- Improving framework detection
- Adding support for another test framework
- Improving the testing checklist
- Adding real-world edge cases
- Improving documentation
- Adding tests for the helper script
- Improving GitHub Actions CI

## Local setup

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the tests:

```bash
python -m pytest
```

## Project structure

```text
skills/test-generator/SKILL.md
```

Main Claude Code Skill instructions.

```text
skills/test-generator/references/testing-checklist.md
```

General testing checklist.

```text
skills/test-generator/references/framework-guides.md
```

Framework-specific testing guidance.

```text
skills/test-generator/scripts/detect_test_framework.py
```

Helper script for detecting the likely test framework used by a project.

```text
tests/test_detect_test_framework.py
```

Automated tests for the helper script.

## Style guidelines

When contributing documentation:

- Use clear language
- Prefer practical examples
- Avoid unnecessary jargon
- Keep examples realistic
- Explain assumptions

When contributing code:

- Keep the script dependency-free unless there is a strong reason
- Add tests for new detection logic
- Prefer simple, readable code
- Avoid over-engineering

## Pull request checklist

Before opening a pull request, please check:

- [ ] The change is within the project scope
- [ ] Documentation is updated if needed
- [ ] Tests are added or updated if code changed
- [ ] `python -m pytest` passes locally
- [ ] Examples are clear and realistic

## Roadmap ideas

Future improvements may include:

- Go testing support
- C# xUnit support
- React Testing Library guidance
- FastAPI route testing guidance
- Spring Boot service testing guidance
- Better framework confidence scoring
- More sample projects
- Test quality scoring