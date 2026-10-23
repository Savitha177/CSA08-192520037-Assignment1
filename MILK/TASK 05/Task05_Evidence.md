
# Task 05 – Read Input and Convert Types

## Aim
To read milk quantity, fat percentage, and SNF percentage from
the user, convert the input strings to numbers, validate the
values, calculate payment, and display a neatly formatted receipt.

## Input and Type Conversion
Python's input() function returns a string.
The program uses strip() to remove surrounding whitespace and
float() to convert valid numeric text into a floating-point number.

The program also replaces a decimal comma with a decimal point,
so an input such as 8,5 can be read as 8.5.

## Handling Invalid Input
The conversion is placed inside a try/except ValueError block.
If the user enters text such as "eight", the program prints an
error message and returns None instead of terminating with an
unhandled conversion error.

The program checks that:
- Milk quantity is not negative.
- Fat percentage is between 2.0 and 7.0.
- SNF percentage is not negative.

## Formatted Output
F-strings display the values in aligned columns.
For example, {amount:8.2f} reserves space for the number and
displays two digits after the decimal point.

## Test Results
1. Quantity 8.5, fat 4.2, SNF 8.7:
   Rate = Rs 33.40 per litre; payment = Rs 283.90.
2. Text input such as "eight":
   The program displays an invalid-number message.
3. Negative quantity:
   The program rejects the value.
4. Fat outside the allowed range:
   The program rejects the value.
5. Decimal-comma input:
   Values such as 8,5 are converted to 8.5.

## Alternative Approach
An alternative is to check the input string before conversion,
using string methods or a numeric-format check. However, these
checks can be difficult to write correctly for all valid numeric
formats. try/except ValueError is a direct way to handle failed
float conversions.

## Complexity
For one entry, the calculation and validation take O(1) time
and O(1) auxiliary space. This assumes each input is treated as
a single value; the time spent reading input depends on its length.
## Input Conversion and Error Handling

Input read from `input()` is initially a string. Numeric conversion is required before calculations can be performed.

A simple pre-check can identify some invalid inputs, but it is difficult to cover every possible string format correctly. Using `try/except ValueError` around numeric conversion is a more direct way to handle text that cannot be converted.

Examples:

- `"8.5"` can be converted to a numeric value.
- `" 8.5 "` can be converted after Python handles surrounding whitespace.
- `"8,5"` needs the program's explicit comma-to-decimal-point conversion if comma decimals are supported.
- `"eight"` cannot be converted to a numeric value and should produce a helpful validation message.

Validation should also check the business rules after conversion: quantity must not be negative, fat must be within the permitted range, and SNF must not be negative.

For a fixed number of inputs, conversion and validation take constant time, O(1). For a list of n entries, validating all entries takes O(n) time.

The program should not crash when the user enters text or an out-of-range measurement.
