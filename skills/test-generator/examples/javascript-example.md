# JavaScript Example: Jest

This example shows how the `test-generator` skill should generate Jest tests for a JavaScript function.

## Input code

File: `src/cart.js`

```javascript
export function calculateTotal(items) {
  return items.reduce((total, item) => {
    return total + item.price * item.quantity;
  }, 0);
}
```

## User request

```text
Use the test-generator skill to generate unit tests for calculateTotal.
Include normal cases, edge cases, and failure cases if relevant.
```

## Expected output

File: `src/cart.test.js`

```javascript
import { calculateTotal } from "./cart";

describe("calculateTotal", () => {
  test("returns the total for a single item", () => {
    const items = [{ price: 10, quantity: 2 }];

    expect(calculateTotal(items)).toBe(20);
  });

  test("returns the total for multiple items", () => {
    const items = [
      { price: 10, quantity: 2 },
      { price: 5, quantity: 3 },
    ];

    expect(calculateTotal(items)).toBe(35);
  });

  test("returns zero for an empty cart", () => {
    expect(calculateTotal([])).toBe(0);
  });

  test("handles items with zero quantity", () => {
    const items = [{ price: 10, quantity: 0 }];

    expect(calculateTotal(items)).toBe(0);
  });
});
```

## Coverage explanation

These tests cover:

- A normal single-item cart
- A normal multi-item cart
- An empty cart edge case
- An item with zero quantity

## Notes

The function assumes every item has a valid `price` and `quantity`.

If invalid items should be rejected, additional tests should check behavior for:

- Missing price
- Missing quantity
- Negative price
- Negative quantity
- Non-array input