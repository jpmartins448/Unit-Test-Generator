# Framework Guides

Use this file when generating tests for Python, JavaScript, TypeScript, or Java projects.

The goal is to match the project's existing test style and use the right framework conventions.

---

# Python: pytest

Prefer `pytest` for Python projects unless the repository clearly uses another framework.

## How to detect pytest

Look for:

- `pytest` in `pyproject.toml`
- `pytest` in `requirements.txt`
- `pytest` in `requirements-dev.txt`
- `pytest` in `setup.cfg`
- Existing files named `test_*.py`
- Existing test functions named `test_*`
- Existing use of `pytest.raises`, `pytest.mark.parametrize`, or fixtures

## File naming

Common pytest file names:

```text
tests/test_calculator.py
test_calculator.py
```

Prefer placing tests in a `tests/` directory if one already exists.

## Imports

Example:

```python
import pytest

from calculator import divide
```

## Normal test

```python
def test_divide_returns_result_for_valid_inputs():
    assert divide(10, 2) == 5
```

## Exception test

```python
def test_divide_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

## Parameterized test

```python
import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (-10, 2, -5),
        (0, 5, 0),
    ],
)
def test_divide_valid_inputs(a, b, expected):
    assert divide(a, b) == expected
```

## Fixture example

```python
import pytest

@pytest.fixture
def sample_user():
    return {
        "id": 1,
        "name": "Alice",
        "active": True,
    }


def test_user_is_active(sample_user):
    assert sample_user["active"] is True
```

## Good pytest style

Prefer:

- Plain `assert`
- `pytest.raises` for exceptions
- `pytest.mark.parametrize` for repeated input/output cases
- Fixtures for reusable setup
- `tmp_path` for temporary files
- `monkeypatch` for environment variables or simple dependency replacement

Avoid:

- Real network calls
- Real production databases
- Overly complex fixtures
- Testing private functions unless necessary
- Repeating implementation logic inside assertions

---

# JavaScript / TypeScript: Jest

Use Jest when the repository has dependencies such as:

- `jest`
- `ts-jest`
- `@types/jest`
- `babel-jest`

Check `package.json` scripts for:

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

## File naming

Common Jest test files:

```text
calculator.test.js
calculator.spec.js
calculator.test.ts
calculator.spec.ts
__tests__/calculator.test.ts
```

## Basic test

```javascript
import { divide } from "./calculator";

describe("divide", () => {
  test("divides positive numbers", () => {
    expect(divide(10, 2)).toBe(5);
  });
});
```

## Exception test

```javascript
import { divide } from "./calculator";

describe("divide", () => {
  test("throws when dividing by zero", () => {
    expect(() => divide(10, 0)).toThrow();
  });
});
```

## Async test

```javascript
test("fetches a user by id", async () => {
  const user = await getUserById(1);

  expect(user).toEqual({
    id: 1,
    name: "Alice",
  });
});
```

## Mock example

```javascript
import { sendEmail } from "./emailService";
import { registerUser } from "./registerUser";

jest.mock("./emailService");

test("sends welcome email after registration", async () => {
  sendEmail.mockResolvedValue(true);

  await registerUser("alice@example.com");

  expect(sendEmail).toHaveBeenCalledWith("alice@example.com");
});
```

## Good Jest style

Prefer:

- `describe` for grouping related tests
- `test` or `it` with clear behavior names
- `expect(...).toBe(...)` for primitive values
- `expect(...).toEqual(...)` for objects/arrays
- `expect(...).toThrow(...)` for exceptions
- Mocks for external dependencies

Avoid:

- Snapshot tests unless they are useful
- Over-mocking internal implementation
- Tests that depend on real timers without controlling them
- Real network calls

---

# JavaScript / TypeScript: Vitest

Use Vitest when the repository has dependencies such as:

- `vitest`
- `vite`
- `@vitest/ui`
- `@vitest/coverage-v8`

Check `package.json` scripts for:

```json
{
  "scripts": {
    "test": "vitest"
  }
}
```

## Basic test

```javascript
import { describe, expect, test } from "vitest";
import { divide } from "./calculator";

describe("divide", () => {
  test("divides positive numbers", () => {
    expect(divide(10, 2)).toBe(5);
  });
});
```

## Exception test

```javascript
import { describe, expect, test } from "vitest";
import { divide } from "./calculator";

describe("divide", () => {
  test("throws when dividing by zero", () => {
    expect(() => divide(10, 0)).toThrow();
  });
});
```

## Mock example

```javascript
import { describe, expect, test, vi } from "vitest";
import { registerUser } from "./registerUser";
import { sendEmail } from "./emailService";

vi.mock("./emailService", () => ({
  sendEmail: vi.fn(),
}));

test("sends welcome email after registration", async () => {
  sendEmail.mockResolvedValue(true);

  await registerUser("alice@example.com");

  expect(sendEmail).toHaveBeenCalledWith("alice@example.com");
});
```

## Good Vitest style

Prefer:

- Explicit imports from `vitest`
- `vi.fn()` and `vi.mock()` for mocks
- Same naming conventions as Jest
- Clear async tests using `async` / `await`

Avoid:

- Mixing Jest globals and Vitest imports unless the project already does that
- Real network calls
- Uncontrolled timers
- Excessive snapshot tests

---

# Java: JUnit 5

Prefer JUnit 5 for Java projects unless the repository clearly uses another test framework.

## How to detect JUnit 5

Look for Maven dependencies in `pom.xml`:

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
</dependency>
```

Look for Gradle dependencies in `build.gradle`:

```gradle
testImplementation 'org.junit.jupiter:junit-jupiter'
```

Look for imports:

```java
import org.junit.jupiter.api.Test;
```

## File naming

Common JUnit test file names:

```text
CalculatorTest.java
UserServiceTest.java
```

Common folder:

```text
src/test/java
```

## Basic test

```java
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class CalculatorTest {

    @Test
    void divideReturnsResultForValidInputs() {
        assertEquals(5, Calculator.divide(10, 2));
    }
}
```

## Exception test

```java
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertThrows;

class CalculatorTest {

    @Test
    void divideThrowsWhenDividingByZero() {
        assertThrows(ArithmeticException.class, () -> Calculator.divide(10, 0));
    }
}
```

## Setup example

```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

class UserServiceTest {

    private UserService userService;

    @BeforeEach
    void setUp() {
        userService = new UserService();
    }

    @Test
    void userIsActiveAfterCreation() {
        User user = userService.createUser("Alice");

        assertTrue(user.isActive());
    }
}
```

## Good JUnit 5 style

Prefer:

- `@Test`
- `@BeforeEach` for reusable setup
- `assertEquals`
- `assertTrue`
- `assertFalse`
- `assertThrows`
- Clear method names written as behavior

Avoid:

- Testing too much in one test method
- Depending on test execution order
- Using real external services in unit tests
- Excessive setup that hides the behavior being tested

---

# Framework selection rules

When choosing a framework:

1. Prefer the framework already used in the repository.
2. If there are existing tests, copy their style.
3. If there is no existing test setup:
   - Use pytest for Python.
   - Use Vitest for Vite-based JavaScript/TypeScript projects.
   - Use Jest for non-Vite JavaScript/TypeScript projects.
   - Use JUnit 5 for Java.
4. If the framework is unclear, state the assumption before generating tests.

---

# Test file location rules

Prefer existing conventions.

If the project has a `tests/` folder, put new tests there.

If the project has tests next to source files, follow that style.

Common defaults:

```text
Python:
  src/calculator.py
  tests/test_calculator.py

JavaScript / TypeScript:
  src/calculator.ts
  src/calculator.test.ts

Java:
  src/main/java/com/example/Calculator.java
  src/test/java/com/example/CalculatorTest.java
```

---

# Final reminder

Generated tests should be realistic code that a developer could copy into the repository and run with minimal edits.