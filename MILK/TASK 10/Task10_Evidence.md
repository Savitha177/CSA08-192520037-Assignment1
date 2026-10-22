# Task 10 – Compare Float and Decimal

## Aim

To compare the accuracy, execution time and memory size of Python `float` and `Decimal` when adding payment amounts.

## Method

The experiment adds 1,000 payments of Rs. 33.40 and three adjustments of Rs. 0.10. Both methods process the same list of 1,003 amounts. The calculation is repeated 1,000 times, and execution time is measured using `perf_counter()`.

## Accuracy

The float calculation produces an internal result similar to `33400.30000000061`. This happens because many decimal fractions cannot be represented exactly in binary floating-point.

The Decimal calculation produces `33400.30` because each amount is created from a decimal string.

## Actual Measurements

- Python version: [Enter the version shown by `python --version`]
- Float execution time: [Copy your measured time]
- Decimal execution time: [Copy your measured time]
- Float memory size: [Copy your measured size]
- Decimal memory size: [Copy your measured size]

Measurements may vary with the computer, Python version and system load.

## Complexity Analysis

For n payment amounts, both methods process each amount once, so the time complexity is O(n).

The running total uses O(1) auxiliary space. The input list itself requires O(n) space and is shared by both methods.

## Conclusion

Float is generally faster and often uses less memory, but it can introduce small representation errors in decimal calculations. Decimal supports exact decimal arithmetic for values constructed from decimal strings and is more suitable for money calculations when the appropriate rounding rules are applied. Both approaches have O(n) time complexity for summing n amounts.
