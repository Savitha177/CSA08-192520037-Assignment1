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
## Comparison of Numeric Approaches

### Float

Python's `float` uses binary floating-point representation. Some decimal fractions cannot be represented exactly, so repeated calculations may produce a small precision difference.

### Decimal

`Decimal` can represent decimal monetary values exactly when it is constructed from strings, for example `Decimal("33.40")`. It is better suited to financial calculations where decimal rounding rules matter.

Avoid constructing money values using `Decimal(33.40)`, because the float approximation may already be present. Prefer `Decimal("33.40")` or `Decimal(str(value))` when the source is a suitable decimal value.

### Integer Paise

Another alternative is to store money as integer paise. For example, Rs 33.40 is stored as 3340 paise. This avoids floating-point representation errors for amounts that are exact multiples of one paisa. Any fractional-paise calculation still needs an explicit rounding rule.

### Rounding Strategy

Rounding each farmer's payment before adding it to the total may produce a different result from adding all unrounded amounts and rounding only once at the end. The program must use the policy required by the co-operative.

### Performance and Memory

`float` is generally faster and uses less memory than `Decimal`, but `Decimal` gives more suitable decimal arithmetic for money. Performance should be measured on the actual workload rather than assumed from one small example.

### Conclusion

For the final payment calculator, use `Decimal` values created from strings and an explicitly documented rounding rule. A small performance cost is acceptable when it improves the correctness and explainability of farmer payments.
