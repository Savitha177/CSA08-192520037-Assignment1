
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
