# Task 2 – Python Values, Types and Decimal Arithmetic

## 1. Python Data Types

- `10` – `int` (integer)
- `10.0` – `float` (decimal number)
- `"10"` – `str` (string)
- `True` – `bool` (Boolean)
- `[10, 8.5]` – `list` (list of values)

## 2. Division Operators

- `7 / 2` gives `3.5` because `/` performs true division.
- `7 // 2` gives `3` because `//` performs floor division.
- `7 % 2` gives `1` because `%` returns the remainder.
- `-7 // 2` gives `-4` because floor division rounds down toward negative infinity.

## 3. Floating-Point Precision

The expression `0.1 + 0.2 == 0.3` returns `False` because many decimal fractions cannot be represented exactly in binary floating-point.

Using `Decimal` with strings, such as `Decimal("0.1")`, gives an exact decimal result for this calculation.

## 4. Money Calculations

The float total is `33400.30000000061`, whereas the Decimal total is `33400.30`.

For money calculations, use `Decimal` created from strings or use integer paise when amounts have two decimal places. Avoid creating Decimal values from floats because the float may already contain an approximation.

## 5. Time and Space Complexity

Both total-calculation methods take O(n) time because each payment is processed once. The running total requires O(1) additional space, excluding the input list.
