# Task 12 – Re-evaluate and Adapt the Design

## 1. Objective

The objective is to modify the existing milk payment calculator to support seasonal rates, fat and SNF readings with two decimal places, and a bonus for farmers supplying more than 500 litres over ten days.

## 2. A. Impact Analysis

The original program used a base rate of Rs 30.00 per litre and a fat adjustment of Rs 0.40 for every 0.1% change. The revised requirements introduce a seasonal base rate of Rs 32.00 and a fat adjustment of Rs 0.45 per 0.1% from April to June.

The analyser also supplies fat and SNF readings to two decimal places. The program must therefore preserve the additional decimal place during the calculation rather than converting readings to integers or rounding the readings prematurely.

The original constants affected are the base rate and fat-step value. The rate calculation and rate-selection functions must also change. A separate bonus function is added to calculate the ten-day bonus.

The revised rate formula is:

Rate = Base rate + Fat adjustment + SNF adjustment

Fat adjustment = ((Fat − 3.5) / 0.1) × Seasonal fat-step value

SNF adjustment = ((SNF − 8.5) / 0.1) × Rs 0.30

The program uses Decimal arithmetic and rounds the calculated rate to two decimal places using ROUND_HALF_UP. This is the rounding policy selected for this implementation and should be confirmed against the co-operative's official accounting policy.

## 3. B. Evaluation of the Original Design

The original design remains useful because its functions, validation, constants and module-based organisation can be reused. A complete redesign is unnecessary.

However, a single fixed rate card is no longer sufficient. The modified design selects a rate card based on the month. From April to June, it uses the revised rate; for other months, it uses the original rate.

Worked examples:

| Season and input | Rate per litre | Payment |
|---|---:|---:|
| Normal season: 10 L, fat 3.50%, SNF 8.50% | Rs 30.00 | Rs 300.00 |
| April: 10 L, fat 3.50%, SNF 8.50% | Rs 32.00 | Rs 320.00 |
| Normal season: 8.5 L, fat 4.20%, SNF 8.70% | Rs 33.40 | Rs 283.90 |
| April: 8.5 L, fat 4.20%, SNF 8.70% | Rs 35.75 | Rs 303.875 before payment rounding |

For the last example, the payment is rounded to Rs 303.88.

These examples demonstrate that seasonal rates affect the result while the reusable calculation functions remain appropriate.

## 4. C. Adaptation or Redesign

I chose to MODIFY the original design.

The updated program includes:

- `select_rate_card()` to select seasonal or normal rates.
- `rate_per_litre()` to calculate the price using the selected rate card.
- `payout()` to calculate and round each delivery payment.
- `bonus_for_ten_days()` to award the bonus only when total ten-day litres exceed 500.
- `calculate_ten_day_payment()` to combine deliveries and calculate the final amount.
- Input validation to reject negative quantities, invalid fat values and negative SNF.

The program uses Decimal values constructed from strings to reduce binary floating-point errors. Rate values and money amounts are rounded to two decimal places according to the chosen policy.

The bonus is calculated as:

Bonus = Total ten-day litres × Rs 0.50, if total litres > 500.

Otherwise, the bonus is Rs 0.00.

For example, a farmer supplying 510 litres qualifies for a bonus of Rs 255.00.

## 5. D. Evidence-Based Defence

The automated tests cover both seasons, two-decimal analyser readings, normal payments, bonus eligibility, and invalid inputs.

| Test | Expected result |
|---|---|
| Normal season, standard readings | Rs 30.00 per litre |
| April, standard readings | Rs 32.00 per litre |
| Normal season, fat 4.20%, SNF 8.70% | Rs 33.40 per litre |
| April, fat 4.20%, SNF 8.70% | Rs 35.75 per litre |
| 510 litres in ten days | Rs 255.00 bonus |
| Exactly 500 litres | No bonus |
| Fat above 7.0% | Reject entry |
| Negative SNF | Reject entry |
| Negative litres | Reject entry |

The tests should be executed in Python, and the actual test output should be saved as evidence.

### Trade-offs

The modified design is more flexible because seasonal changes can be managed through rate selection rather than duplicating the calculation logic. Decimal arithmetic supports predictable decimal calculations, although it can be slower and use more memory than float arithmetic.

The main limitation is that the program uses a fixed set of seasonal rules and a simple interactive interface. Future changes to rate periods, bonus eligibility or official rounding rules would require updating the relevant configuration or functions.

For a district union, the functions can be reused, but a production system would also need persistent storage, secure access, audit logs, duplicate-entry protection and stronger operational testing.

## 6. Conclusion

The original design should be modified rather than retained unchanged or completely redesigned. Its reusable functions and validation remain suitable, while seasonal rate selection, two-decimal readings and ten-day bonus calculation address the new requirements. Automated test results provide evidence that the revised design handles both seasons and the bonus rule.