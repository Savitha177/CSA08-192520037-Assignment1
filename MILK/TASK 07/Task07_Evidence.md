
# Task 07 – Build a Module

## Aim
To store the milk rate constants and calculation functions in
milkrate.py and reuse them from a separate Python script.

## Module Implementation
The milkrate.py file contains the rate constants,
rate_per_litre(), and payout().

TODO 1 was completed by calculating the fat and SNF steps,
adding their adjustments to the base rate, and rounding the rate
to two decimal places.

TODO 2 was completed by multiplying the quantity of milk by
the calculated rate and rounding the payment to two decimal places.

## Import Methods
1. import milkrate:
   Access functions using milkrate.payout(...).

2. from milkrate import payout:
   Access the imported function directly using payout(...).

3. import milkrate as mr:
   Use the alias mr to access module functions, such as mr.payout(...).

## The __name__ Condition
The condition if __name__ == "__main__": ensures that the
demonstration runs when milkrate.py is executed directly.
When the module is imported by test_milkrate.py, the demonstration
does not run.

Without this condition, top-level demonstration code would run
during import.

## Standard Library and Module Search
Python provides standard-library modules such as math and decimal.
The math module contains mathematical functions, while decimal
supports decimal arithmetic.

Python searches for importable modules using locations listed
in sys.path, including the script's directory in a normal
script execution. Python caches imported modules in sys.modules
within the current process.

## Test Results
Direct module execution:
- 10 L, fat 3.5, SNF 8.5: rate Rs 30.00, payment Rs 300.00.
- 8.5 L, fat 4.2, SNF 8.7: rate Rs 33.40, payment Rs 283.90.
- 12 L, fat 3.1, SNF 8.3: rate Rs 27.80, payment Rs 333.60.

Separate script import:
- payout(8.5, 4.2, 8.7) returns 283.9.
- payout(10, 3.5, 8.5) returns 300.0.
- payout(12, 3.1, 8.3) returns 333.6.

The demonstration table does not print when the module is imported.

## Alternative Concept
Copying the functions into every script duplicates code.
When a rate changes, every copy must be updated, increasing
the chance of inconsistent calculations. A shared module allows
the calculation to be maintained in one place.

## Complexity Analysis
A single rate or payout calculation takes O(1) time and O(1)
auxiliary space.

Processing n milk entries takes O(n) time and O(1) auxiliary
space when results are accumulated without storing a second list.
Module import has a one-time loading cost and the module is
cached in sys.modules for reuse within the same process.
## Unit Test Results

The Task 7 milk-rate module was tested using Python's `unittest` framework.

Four tests were executed:
- Standard milk rate: passed.
- Higher fat and SNF rate: passed.
- Lower fat and SNF rate: passed.
- Standard payment calculation: passed.

**Result:** 4 tests passed, with no failures or errors.

The terminal output screenshot is included as test evidence.