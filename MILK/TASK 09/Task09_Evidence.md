# Task 09 – Implement and Test the Milk Payment Calculator

## Aim

To implement a Python milk payment calculator and test correct calculations, input validation and payment totals.

## Implementation

The program uses named constants and `Decimal` for monetary calculations. It uses functions to calculate the rate per litre, calculate payments and validate each farmer's entry.

Valid entries are processed. Invalid entries display an error and are skipped.

## Test Results

| Test | Expected result |
|---|---|
| Quantity 10 L, fat 3.5%, SNF 8.5% | Rate Rs. 30.00; payment Rs. 300.00 |
| Quantity 8.5 L, fat 4.2%, SNF 8.7% | Rate Rs. 33.40; payment Rs. 283.90 |
| Quantity 12 L, fat 3.1%, SNF 8.3% | Rate Rs. 27.80; payment Rs. 333.60 |
| Negative quantity | Rejected |
| Fat below 2.0% | Rejected |
| Fat above 7.0% | Rejected |
| Negative SNF | Rejected |
| Comma decimal input | Converted successfully |

## Automatic Testing

The test file `test_task09_calculator.py` contains nine unit tests. Run them using:

`python -m unittest -v test_task09_calculator.py`

Record the actual result after executing the tests.

## Complexity Analysis

For n farmer entries, each entry requires a fixed number of validation and calculation operations. Therefore, processing time is O(n).

The program stores a running total for each distinct farmer ID. If there are u distinct farmers, the additional storage for these totals is O(u). The program does not need to store every individual entry.

## Conclusion

The calculator computes the expected payments, rejects invalid entries, accepts decimal input and produces a summary of valid payments. Automatic tests are used to verify its calculation and validation functions.
