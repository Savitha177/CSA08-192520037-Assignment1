# Task 10 — Performance and Precision Comparison

## Objective

This task compares floating-point arithmetic and Decimal arithmetic at 300, 6,000 and 150,000 payments. It also compares two rounding policies and demonstrates a dictionary-based rate lookup alternative.

## Method

The program uses `time.perf_counter()` to measure elapsed time. Each total calculation is repeated three times to reduce the effect of a single unusually short measurement. The timings are measurements from this computer and may differ on another system.

## Results

Copy the actual totals and timings from the terminal output for all three payment counts. Include the Python version and machine details if available.

| Payment count | Float total | Decimal total | Float time | Decimal time |
|---:|---:|---:|---:|---:|
| 300 | Fill from output | Fill from output | Fill from output | Fill from output |
| 6,000 | Fill from output | Fill from output | Fill from output | Fill from output |
| 150,000 | Fill from output | Fill from output | Fill from output | Fill from output |

Do not leave these placeholders in the submitted report. Use the real output produced by the final submitted program.

## Rounding Comparison

The program demonstrates rounding every payment to two decimal places before addition versus adding the exact Decimal values and rounding the total once. The results can differ when individual amounts contain fractions of a paisa.

The correct policy depends on the co-operative's payment rules. If each farmer must be paid to the nearest paisa, round each farmer's payment at that payment boundary and add those rounded payments to obtain the payable total.

## Dictionary Alternative

A dictionary can map known rate-card keys to rate values. Average dictionary lookup is O(1), while building or loading a dictionary with k entries takes O(k) time and O(k) space.

The example measures a small dictionary lookup loop. It is not a complete substitute for calculating rates for arbitrary fat and SNF readings unless the dictionary contains all required cases or the program has a defined fallback strategy.

## Memory

The program prints the shallow object sizes for one float and one Decimal value. These values are examples, not the complete memory cost of a list of payments or a running calculator.

## Conclusion

Float is generally faster and smaller, but can accumulate binary representation error. Decimal is more appropriate for financial calculations because decimal values and rounding rules can be represented explicitly. The final design should prioritize correct payment amounts, transparent rounding and sufficient performance for the required workload.
