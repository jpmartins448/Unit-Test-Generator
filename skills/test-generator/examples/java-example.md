# Java Example: JUnit 5

This example shows how the `test-generator` skill should generate JUnit 5 tests for a Java class.

## Input code

File: `src/main/java/com/example/PasswordValidator.java`

```java
package com.example;

public class PasswordValidator {

    public boolean isValid(String password) {
        if (password == null) {
            return false;
        }

        return password.length() >= 8;
    }
}
```

## User request

```text
Use the test-generator skill to generate JUnit 5 tests for PasswordValidator.
Include normal cases, edge cases, and failure cases.
```

## Expected output

File: `src/test/java/com/example/PasswordValidatorTest.java`

```java
package com.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PasswordValidatorTest {

    private PasswordValidator validator;

    @BeforeEach
    void setUp() {
        validator = new PasswordValidator();
    }

    @Test
    void returnsTrueWhenPasswordHasAtLeastEightCharacters() {
        assertTrue(validator.isValid("password123"));
    }

    @Test
    void returnsFalseWhenPasswordIsTooShort() {
        assertFalse(validator.isValid("short"));
    }

    @Test
    void returnsTrueWhenPasswordHasExactlyEightCharacters() {
        assertTrue(validator.isValid("12345678"));
    }

    @Test
    void returnsFalseWhenPasswordIsNull() {
        assertFalse(validator.isValid(null));
    }

    @Test
    void returnsFalseWhenPasswordIsEmpty() {
        assertFalse(validator.isValid(""));
    }
}
```

## Coverage explanation

These tests cover:

- Valid passwords longer than the minimum length
- Passwords shorter than the minimum length
- The exact boundary value of eight characters
- Null input
- Empty string input

## Notes

The current production code only validates password length.

If the intended behavior includes stronger password rules, additional tests should cover:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Whitespace-only passwords