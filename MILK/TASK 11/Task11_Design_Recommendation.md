# Task 11 – Recommend and Defend the Final Design

## 1. Aim

The aim of this task is to recommend a suitable design for the Ksheera Village Milk Producers’ Co-operative payment calculator. The design must calculate payments accurately, validate inputs, make rate revisions manageable and remain suitable when the number of farmers increases.

## 2. Recommended Data Types and Rounding Rule

I recommend using Python's `Decimal` type for money-related calculations instead of relying on `float`.

A `float` stores numbers in binary floating-point form. Some decimal values cannot be represented exactly, which can cause small differences in financial totals. In my Task 10 experiment, the float result was approximately `33400.30000000061`, while the Decimal result was `33400.30`.

I recommend creating Decimal values from strings, for example `Decimal("30.00")`, to preserve the intended decimal values.

The program should calculate the rate and payment using Decimal arithmetic. Each farmer's payment should be rounded to two decimal places using a clearly defined rule, such as `ROUND_HALF_UP`, before it is added to the farmer's ten-day total. This makes the rounding policy consistent and easier to explain.

The co-operative should confirm its official accounting rule before using the calculator for real payments.

## 3. Managing Rate Revisions

The base rate, standard fat, standard SNF, fat adjustment and SNF adjustment should be stored as named constants in one module, such as `milkrate.py`.

This is better than repeating rate values throughout the program. When the co-operative announces a rate revision, the relevant constants can be updated in one place, reducing the chance of inconsistent changes.

The calculation functions should use these constants rather than hard-coded numbers. Unit tests should be run after every revision to check the expected rates and payments.

## 4. Validation and Testing

The calculator should validate every entry before calculating a payment.

- Milk quantity must not be negative.
- Fat must be within the specified range of 2.0% to 7.0%.
- SNF must not be negative.
- Invalid numeric input should produce a clear error message rather than crashing the program.

The program should also be tested with valid examples, boundary values, invalid entries and multiple deliveries from the same farmer.

The original assignment examples are:

| Litres | Fat | SNF | Expected rate | Expected payment |
|---:|---:|---:|---:|---:|
| 10 | 3.5 | 8.5 | Rs 30.00 | Rs 300.00 |
| 8.5 | 4.2 | 8.7 | Rs 33.40 | Rs 283.90 |
| 12 | 3.1 | 8.3 | Rs 27.80 | Rs 333.60 |

These expected results should be compared with the program's actual output and unit-test results.

## 5. Limitations of the Design

The current command-line calculator has some limitations:

1. Data may be lost when the program closes unless records are saved to a file or database.
2. Manual entry can cause typing mistakes.
3. The program does not provide a graphical interface for clerks.
4. A single-user program does not automatically support multiple collection centres or simultaneous users.
5. Rate changes require a controlled update and retesting process.
6. Decimal arithmetic improves financial precision, but the program must still use the correct formula, rounding policy and validated input values.

For practical deployment, the co-operative should add persistent records, backups, access controls and an audit trail.

## 6. Suitability at District-Union Scale

The calculator's core rate and payment functions are suitable for reuse at a larger scale because they perform small, independent calculations.

If there are n milk entries, processing each entry once takes O(n) time. If entries are processed one at a time and only running totals are retained, the calculation itself can use O(1) auxiliary space. If all entries are stored in memory, the storage requirement grows to O(n).

At district-union scale, the system should use a database, indexed farmer records, transaction handling, backups and access controls. Large reports can be processed in batches. The calculation functions can remain reusable, but the complete command-line program would need additional infrastructure.

## 7. Alternative Design: Read a Rate Card from a JSON File

Instead of keeping rate values directly in a Python module, the program could read them from a JSON file when it starts.

Example `ratecard.json`:

```json
{
  "base_rate": "30.00",
  "standard_fat": "3.5",
  "standard_snf": "8.5",
  "fat_step_value": "0.40",
  "snf_step_value": "0.30",
  "min_fat": "2.0",
  "max_fat": "7.0"
}
```

The program could load the file using Python's `json` module and convert the decimal strings to `Decimal` values.

Example:

```python
import json
from decimal import Decimal

with open("ratecard.json", "r", encoding="utf-8") as file:
    rate_card = json.load(file)

BASE_RATE = Decimal(rate_card["base_rate"])
STANDARD_FAT = Decimal(rate_card["standard_fat"])
STANDARD_SNF = Decimal(rate_card["standard_snf"])
FAT_STEP_VALUE = Decimal(rate_card["fat_step_value"])
SNF_STEP_VALUE = Decimal(rate_card["snf_step_value"])
```

### Complexity comparison

Let t be the number of values in the rate card.

- **Reading the JSON file:** startup time is O(t), because the program reads and processes the rate-card values. The loaded rate card occupies O(t) space.
- **Constants in a Python module:** the values are loaded when the module is imported. There is no separate JSON-reading step, and the storage for the fixed set of constants is O(1) with respect to the number of milk entries.
- **Calculating a payment:** remains O(1) per entry for either design.
- **Editing and distributing changes:** with constants in the module, a revision generally requires changing and redistributing the program. With a JSON rate card, an authorised user can update the configuration file without changing the calculation functions, provided the file format remains compatible.

For a small fixed rate card, the startup cost of reading JSON should be small, but it must be measured on the actual system. The JSON approach also requires error handling for missing, malformed or invalid configuration values.

## 8. Evidence from Experiments

In Task 10, I compared the results and performance of `float` and `Decimal`. I will use the actual measurements from my run below.


| Measurement | Actual result |
|---|---:|
| Number of payments | 1,003 |
| Float total | Rs 33,400.30 |
| Decimal total | Rs 33,400.30 |
| Float exact representation | 33,400.30000000061 |
| Decimal exact result | 33,400.30 |
| Repeats per method | 1,000 |
| Float calculation time | 0.063935 seconds |
| Decimal calculation time | 0.179286 seconds |
| Decimal / float time ratio | 2.80x |
| Memory size of one float value | 24 bytes |
| Memory size of one Decimal value | 120 bytes |
| JSON rate-card loading time | 0.00038990 seconds |

### Discussion of Results

Both float and Decimal produced the same displayed total of Rs 33,400.30 for 1,003 payments. However, the float's exact representation was 33,400.30000000061, demonstrating a small binary floating-point representation difference. Decimal produced the exact decimal result of 33,400.30.

In this experiment, Decimal took 0.179286 seconds, while float took 0.063935 seconds. Therefore, Decimal took approximately 2.80 times as long as float. The reported memory size of one Decimal value was 120 bytes, compared with 24 bytes for one float value.

Although float was faster and used less memory in this test, Decimal is recommended for the co-operative's monetary calculations because it supports predictable decimal arithmetic. The official payment-rounding rule should also be applied consistently.

The rate-card loading time was not measured in this experiment.

The float and Decimal timing results depend on the computer, Python version and workload. I will not assume that one timing result applies to every system.

## 9. Final Recommendation

I recommend retaining the modular calculator design, using `Decimal` for money-related calculations, named constants for the rate rules, reusable functions for rate and payment calculations, and validation before processing entries.

For the current small co-operative, a Python module containing the rate constants is simple and sufficient. If rates change frequently or different centres need different rate cards, loading a validated JSON configuration file would make revisions easier without changing the calculation logic.

For district-union use, I would retain the tested calculation functions but add database storage, access control, audit records, backups and batch processing.

This recommendation is based on the expected payment examples, the validation and unit tests from Task 9, and the actual numerical and timing observations recorded in Task 10.
## Rate Card Loading and Complexity

The rate card is stored in a JSON file and loaded when the program starts. In my recorded run, the JSON loading time was **0.00038990 seconds**. This time may vary depending on the computer and execution.

- **Startup time:** Loading a rate card containing *k* entries takes O(k) time.
- **Memory usage:** Storing the loaded rate card takes O(k) space.
- **Per-payment calculation:** O(1), assuming a fixed number of calculations.
- **Maintenance:** Updating rates in the JSON file allows rate changes without editing the Python source code.
- **Limitation:** The program should validate the JSON data and handle missing or invalid configuration files safely.