# Task 4 – Write Correct Expressions

## 1. Expressions for the milk rate and payment

Fat steps are calculated using:

`round((fat - 3.5) / 0.1)`

SNF steps are calculated using:

`round((snf - 8.5) / 0.1)`

The rate per litre is:

`BASE_RATE + fat_steps * 0.40 + snf_steps * 0.30`

The payment is:

`round(litres * rate, 2)`

The `round()` function is used to convert the calculated step count to the nearest whole step and to round the payment to two decimal places.

## 2. Operator precedence and associativity

Python evaluates exponentiation before unary minus. Therefore, `-2 ** 2` evaluates to `-4`, while `(-2) ** 2` evaluates to `4`.

Exponentiation associates from right to left. Thus, `2 ** 3 ** 2` means `2 ** (3 ** 2)` and evaluates to `512`.

Parentheses make the intended order of calculation clear.

## 3. Unexpected expression results

- `(4.2 - 3.5) / 0.1` can produce `7.000000000000001` instead of exactly `7` because decimal fractions are not always represented exactly in binary floating-point.
- `0.1 + 0.2` produces a value close to `0.3`, so `0.1 + 0.2 == 0.3` evaluates to `False`.
- `-2 ** 2` evaluates to `-4`, not `4`, because exponentiation is evaluated before unary minus.

Rounding the step count helps avoid an incorrect step caused by small floating-point errors.

## 4. Difference between round(), int() and math.floor()

`round()` rounds to the nearest integer, subject to Python's tie-rounding rules. `int()` truncates the fractional part toward zero. `math.floor()` rounds down toward negative infinity.

For fat = 4.2, the raw step count is approximately 7.000000000000001. All three methods give 7 steps in this case, producing a fat-adjusted rate of Rs 32.80.

For fat = 3.1, the raw step count is approximately -3.9999999999999996. `round()` gives -4 steps and a rate of Rs 28.40. `int()` gives -3 steps and a rate of Rs 28.80. `math.floor()` gives -4 steps and a rate of Rs 28.40.

Therefore, `int()` is not appropriate for negative step counts in this example.

## 5. Chained comparisons and Boolean operators

The expression `2.0 <= fat <= 7.0` checks whether fat is between 2.0 and 7.0, including both boundaries.

The expression `2.0 <= fat <= 7.0 and snf >= 0` requires both conditions to be true. The `and` operator combines the conditions.

## 6. Alternative concept and complexity

The alternative implementations use `int()` or `math.floor()` instead of `round()` to calculate fat steps. Their step-count operations take O(1) time and O(1) additional space, just like `round()`.

However, the results can differ for negative values. For fat = 3.1, `int()` truncates the approximately -4 step count toward zero and gives -3, while `round()` and `math.floor()` give -4.

Using `round()` is the chosen approach for this task because it is specified in the assignment and handles the demonstrated floating-point step-count error. Money calculations in a production payment system should additionally use exact decimal arithmetic or integer paise to avoid accumulated floating-point errors.
