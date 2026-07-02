# Testing Checklist

Use this checklist when generating, improving, or reviewing unit tests.

The goal is to create tests that are useful, readable, deterministic, and likely to catch real bugs.

## 1. Understand the target code

Before writing tests, identify:

- What the function, class, or module is supposed to do
- Its inputs
- Its outputs
- Its side effects
- Its dependencies
- Its error behavior
- Any assumptions that are not explicit in the code

If behavior is unclear, state the assumption before generating tests.

## 2. Normal cases

Generate tests for expected, common usage.

Examples:

- Valid input with typical values
- Common successful path
- Standard return value
- Expected object/state change
- Expected API response
- Expected parsing or formatting behavior

A normal-case test should answer:

> Does the code work when used correctly?

## 3. Edge cases

Look for boundary or unusual values.

Common edge cases include:

- Empty strings
- Empty arrays/lists
- Null, None, undefined, or missing values
- Zero
- Negative numbers
- Very large numbers
- One item
- Duplicate values
- Whitespace-only strings
- Unicode or special characters
- Minimum and maximum allowed values
- Case sensitivity
- Sorting or ordering edge cases

An edge-case test should answer:

> Does the code behave correctly near the limits of expected input?

## 4. Failure cases

Generate tests for invalid or exceptional situations.

Examples:

- Invalid input type
- Missing required argument
- Invalid format
- Division by zero
- File not found
- Permission error
- External service failure
- Timeout
- Failed validation
- Duplicate resource
- Unauthorized access

A failure-case test should answer:

> Does the code fail safely and clearly?

## 5. Side effects

If the code has side effects, test them carefully.

Common side effects:

- Writing to a file
- Calling an API
- Sending a message
- Updating a database
- Logging
- Modifying global state
- Mutating input objects
- Publishing an event
- Changing time-dependent state

Prefer mocking or dependency injection for external side effects.

Avoid real network calls, real production databases, or irreversible actions in unit tests.

## 6. Determinism

Tests should produce the same result every time.

Control or avoid:

- Current time/date
- Randomness
- Network calls
- Race conditions
- File system state
- Environment variables
- Database state
- Test execution order

If the code depends on time, inject the clock or freeze time.

If the code depends on randomness, inject a seed or mock the random generator.

## 7. Independence

Each test should be independent.

Avoid tests that:

- Depend on another test running first
- Share mutable state without cleanup
- Reuse global state carelessly
- Depend on external services being available
- Depend on local machine configuration

Each test should be able to run alone.

## 8. Assertions

Assertions should be meaningful.

Prefer assertions that check behavior directly.

Good assertions:

- Check returned values
- Check raised exceptions
- Check relevant state changes
- Check calls to mocked dependencies
- Check output structure
- Check important fields

Weak assertions:

- Only checking that result is not null
- Only checking that no exception was thrown
- Repeating the implementation logic inside the test
- Checking private implementation details without a strong reason

## 9. Test names

Test names should describe behavior.

Prefer names like:

- `test_returns_total_for_valid_items`
- `test_raises_error_when_email_is_invalid`
- `shouldReturnUserWhenIdExists`
- `divideThrowsWhenDividingByZero`

Avoid vague names like:

- `test_1`
- `test_function`
- `test_success`
- `test_error`

A good test name explains what broke when the test fails.

## 10. Fixtures and setup

Use fixtures when multiple tests need the same setup.

Good fixture candidates:

- Sample user
- Temporary file
- Mock service
- Test database object
- Reusable configuration
- Common input payload

Avoid fixtures when they hide important details and make tests harder to understand.

Prefer local setup inside the test when the setup is small and relevant.

## 11. Mocks

Use mocks for external dependencies, not for everything.

Good mocking targets:

- Network clients
- Payment providers
- Email/SMS senders
- Databases in unit tests
- File systems when file I/O is not the behavior being tested
- Time providers
- Random generators

Avoid excessive mocking because it can make tests too dependent on implementation details.

## 12. Parameterized tests

Use parameterized tests when the same behavior should be checked for many inputs.

Good use cases:

- Multiple valid input/output pairs
- Validation rules
- Boundary values
- Formatting cases
- Parsing cases

Avoid parameterization if each case needs a different explanation or setup.

## 13. What to explain after generating tests

After generating tests, explain:

- What normal cases are covered
- What edge cases are covered
- What failure cases are covered
- What mocks or fixtures were used
- What assumptions were made
- What is still not tested
- Any refactor that would make the code easier to test

## 14. Red flags in code under test

Mention these issues if they make testing harder:

- Large function with many responsibilities
- Hidden global state
- Direct network/database calls inside business logic
- Hard-coded current time
- Hard-coded randomness
- No clear error behavior
- No clear return type
- Tight coupling to framework code
- Logic mixed with I/O
- Private methods containing most of the business logic

Suggest small refactors, but do not rewrite the production code unless asked.