# Task 1 – Understand the Problem and Identify the Data

## 1. Problem Description

The village milk co-operative collects milk from farmers during morning and evening shifts. The calculator uses the quantity of milk, fat percentage and SNF percentage to calculate the rate per litre and the payment due to each farmer. Correct monetary calculations are important because farmers are paid every ten days.

## 2. Inputs and Outputs

| Value | Data type | Purpose |
|---|---|---|
| Farmer ID | String (`str`) | Identifies the farmer |
| Milk quantity in litres | Decimal number | Records the quantity supplied |
| Fat percentage | Decimal number | Used to calculate the rate |
| SNF percentage | Decimal number | Used to calculate the rate |
| Shift | String (`str`) | Records morning or evening collection |
| Rate per litre | Decimal number | Stores the calculated milk rate |
| Payment amount | Decimal number | Stores the amount owed to the farmer |
| Ten-day total | Decimal number | Stores the total payment for the period |

The `Decimal` type is suitable for monetary calculations because it avoids many binary floating-point representation errors associated with `float`.

## 3. Named Constants

The original rate card uses these constants:

- `BASE_RATE = Decimal("30.00")`: the standard rate per litre.
- `STANDARD_FAT = Decimal("3.5")`: the reference fat percentage.
- `STANDARD_SNF = Decimal("8.5")`: the reference SNF percentage.
- `FAT_STEP_VALUE = Decimal("0.40")`: the rate adjustment for each 0.1% fat step.
- `SNF_STEP_VALUE = Decimal("0.30")`: the rate adjustment for each 0.1% SNF step.
- `STEP_SIZE = Decimal("0.1")`: the percentage difference represented by one step.
- `MIN_FAT = Decimal("2.0")` and `MAX_FAT = Decimal("7.0")`: the accepted fat limits.

These values are named constants so that rate changes can be made in one place rather than changing numbers throughout the program.

## 4. Validation Rules

1. Farmer ID must not be empty.
2. Milk quantity must not be negative.
3. Fat percentage must be between 2.0% and 7.0%, inclusive.
4. SNF percentage must not be negative.
5. Shift must be either Morning or Evening.
6. Numeric inputs must be valid finite numbers.
7. The calculated rate and payment are rounded to two decimal places.

These checks prevent invalid entries from being used to calculate payments.

## 5. Assumptions

- The original standard rate is Rs 30.00 per litre at 3.5% fat and 8.5% SNF.
- Every 0.1% fat step changes the rate by Rs 0.40 per litre.
- Every 0.1% SNF step changes the rate by Rs 0.30 per litre.
- The supplied quantity is measured in litres.
- Each valid entry belongs to one farmer and one collection shift.
- The original rate card applies unless a later requirement specifies a seasonal rate card.
- Payment values are represented to two decimal places.

## 6. Alternative Design: Separate Variables Versus a List

For 300 farmers, using separate variables such as `litres1`, `fat1`, `snf1`, `litres2`, `fat2` and `snf2` would create many variables and make the program difficult to maintain. Adding more farmers would require more manually written variables and calculations.

A list or tuple can group the data for each farmer, for example:

`(farmer_id, litres, fat, snf, shift)`

The program can process these entries using a loop. Processing n entries takes O(n) time. Storing all n entries takes O(n) space. If only a running total is required and the entries do not need to be retained, the calculation can use O(1) additional space.

The list or tuple design is more maintainable and scales more easily as the number of farmers increases.

## 7. Conclusion

The calculator uses named constants, Decimal arithmetic, functions and input validation to improve accuracy and maintainability. Grouping farmer data into structured entries and processing them with loops makes the design easier to extend from a village collection centre to a larger co-operative.