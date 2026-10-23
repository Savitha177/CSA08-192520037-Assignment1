# Task 08 – Algorithm Design

## 1. Aim

To design an algorithm, pseudocode and flowchart for calculating milk payments for farmers in a village milk co-operative.

## 2. Input

- Farmer ID
- Quantity of milk in litres
- Fat percentage
- SNF percentage
- Number of farmer entries to process

## 3. Constants and Business Rules

- Base rate: Rs. 30.00 per litre
- Base fat: 3.5%
- Base SNF: 8.5%
- Rate adjustment for every 0.1% fat difference: Rs. 0.40 per litre
- Rate adjustment for every 0.1% SNF difference: Rs. 0.30 per litre
- Milk quantity must be non-negative.
- Fat must be between 2.0% and 7.0%, inclusive.
- SNF must be non-negative.
- Invalid entries must display an error and be skipped.

## 4. Algorithm

1. Start the program.
2. Set the base rate, base fat, base SNF and total payment.
3. Read the number of farmer entries.
4. For each entry, read the farmer ID, milk quantity, fat percentage and SNF percentage.
5. Check whether the milk quantity is non-negative.
6. Check whether fat is between 2.0% and 7.0%.
7. Check whether SNF is non-negative.
8. If any validation fails, display an error and skip that entry.
9. For a valid entry, calculate the difference between the measured fat and base fat, and between the measured SNF and base SNF.
10. Calculate the rate per litre:

    Rate = 30 + ((Fat − 3.5) / 0.1 × 0.40) + ((SNF − 8.5) / 0.1 × 0.30)

11. Calculate payment = milk quantity × rate per litre.
12. Add the valid payment to the total payment.
13. Display the farmer's rate and payment.
14. Repeat until all entries have been processed.
15. Display the total payment for valid entries.
16. Stop.

## 5. Pseudocode

```text
START

SET base_rate = 30.00
SET base_fat = 3.5
SET base_snf = 8.5
SET total_payment = 0

INPUT number_of_entries

FOR each entry from 1 to number_of_entries

    INPUT farmer_id, litres, fat, snf

    IF litres < 0 THEN
        DISPLAY "Invalid milk quantity"
        SKIP current entry

    ELSE IF fat < 2.0 OR fat > 7.0 THEN
        DISPLAY "Invalid fat percentage"
        SKIP current entry

    ELSE IF snf < 0 THEN
        DISPLAY "Invalid SNF percentage"
        SKIP current entry

    ELSE
        fat_difference = fat - base_fat
        snf_difference = snf - base_snf

        rate = base_rate
               + (fat_difference / 0.1 * 0.40)
               + (snf_difference / 0.1 * 0.30)

        payment = litres * rate
        total_payment = total_payment + payment

        DISPLAY farmer_id, rate, payment
    END IF

END FOR

DISPLAY total_payment

STOP
```

## 6. Test Cases

| Milk (L) | Fat (%) | SNF (%) | Expected result |
|---:|---:|---:|---|
| 10 | 3.5 | 8.5 | Rate Rs. 30.00; payment Rs. 300.00 |
| 8.5 | 4.2 | 8.7 | Rate Rs. 33.40; payment Rs. 283.90 |
| 12 | 3.1 | 8.3 | Rate Rs. 27.80; payment Rs. 333.60 |
| -2 | 3.5 | 8.5 | Reject: invalid quantity |
| 5 | 1.5 | 8.5 | Reject: fat below minimum |
| 5 | 3.5 | -1 | Reject: invalid SNF |

## 7. Complexity Analysis

- Time complexity: O(n), where n is the number of farmer entries.
- Auxiliary space complexity: O(1), when each entry is processed individually without storing all entries.

## 8. Conclusion

The algorithm defines the input, validation, rate calculation, farmer payment calculation and total payment calculation before implementation. The flowchart represents the same processing steps and validation decisions.
## Hand Trace of Three Entries

Initial running total = Rs 0.00.

| Entry | Quantity | Fat | SNF | Rate per litre | Payment | Running total |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 10 L | 3.5% | 8.5% | Rs 30.00 | Rs 300.00 | Rs 300.00 |
| 2 | 8.5 L | 4.2% | 8.7% | Rs 33.40 | Rs 283.90 | Rs 583.90 |
| 3 | 12 L | 3.1% | 8.3% | Rs 27.80 | Rs 333.60 | Rs 917.50 |

The running total after all three entries is Rs 917.50.

## Alternative: Store All Entries in a List

One design stores every entry in a list and calculates the total after collecting the data. This is useful when records must be reviewed or recalculated, but it requires O(n) additional storage for n entries.

A running-total design updates the total as each entry is processed. It requires O(1) auxiliary storage for the total, excluding any farmer records that must be retained for other reasons.

Both approaches take O(n) time to process n entries. The better choice depends on whether the co-operative needs the full transaction history or only the aggregate total.
