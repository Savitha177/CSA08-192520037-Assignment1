
# Task 06 – Organise the Logic into Functions

## Aim
To organise the milk payment calculator into reusable functions
and understand parameters, return values, local variables,
global constants, and docstrings.

## Functions Implemented

### 1. rate_per_litre(fat, snf)
Accepts fat and SNF as parameters and returns the calculated
rate per litre.

### 2. payout(litres, fat, snf)
Uses the rate_per_litre() function and returns the payment for
one milk entry.

### 3. ten_day_total(entries)
Accepts a list of milk entries and returns the sum of their
payments. Each entry contains litres, fat, and SNF.

### 4. main()
Calls the other functions and displays the results.

## Parameters and Return Values
Parameters pass input values into functions.
The return statement sends a result back to the caller.
The print() function displays information but does not replace
a returned calculation result.

## Local Variables and Global Constants
BASE_RATE, STANDARD_FAT, STANDARD_SNF, FAT_STEP_VALUE,
SNF_STEP_VALUE, and STEP_SIZE are global constants by naming
convention. Python does not strictly enforce constants, so
the program avoids changing these values inside functions.

Variables such as total and rate are local to the functions
where they are created.

## Docstrings
Each function has a docstring explaining its purpose,
inputs, or returned result.

## Test Results
1. 10 litres, fat 3.5, SNF 8.5:
   Rate = Rs 30.00; payment = Rs 300.00.
2. 8.5 litres, fat 4.2, SNF 8.7:
   Rate = Rs 33.40; payment = Rs 283.90.
3. 12 litres, fat 3.1, SNF 8.3:
   Rate = Rs 27.80; payment = Rs 333.60.
4. Total payment for these three entries = Rs 917.50.

## Alternative Concept
An alternative is to write all calculations in one long script
without separate functions. This may appear shorter for a tiny
program, but repeated calculations and output logic can make
maintenance and testing harder.

With functions, the calculation can be reused and tested
independently. Function calls have a small overhead, but the
rate and payment calculations still take constant time per entry.

## Complexity Analysis
rate_per_litre(): O(1) time and O(1) auxiliary space.
payout(): O(1) time and O(1) auxiliary space.
ten_day_total(): O(n) time for n entries and O(1) auxiliary
space for its running total, excluding the input list.
The total function does not create another list of payments.
## Why Functions Are Used

The program separates rate calculation, payment calculation and ten-day total calculation into functions. This makes the logic easier to test and reuse.

An alternative is to put all calculations into one long script. That may appear shorter initially, but it duplicates logic and makes individual parts harder to test and maintain.

A lambda expression can represent a short function, but it is not automatically a better choice. Named functions are preferable when the calculation has a business meaning, needs validation or benefits from a clear explanation.

Function calls have a small runtime overhead. For this assignment, the clarity, reuse and testability of named functions are more important than that small overhead.

The time required to calculate one payment is O(1), assuming each calculation uses a fixed number of operations. Processing n payments takes O(n) time.
