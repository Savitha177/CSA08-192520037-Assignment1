
"""Task 4: Write correct expressions for milk payment."""

import math

BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STEP_SIZE = 0.1


def rate_with_round(fat, snf):
    """Calculate the rate using rounded fat and SNF step counts."""
    fat_steps = round((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / STEP_SIZE)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def rate_with_int(fat):
    """Calculate a rate using int() for the fat step count."""
    steps = int((fat - STANDARD_FAT) / STEP_SIZE)
    return round(BASE_RATE + steps * FAT_STEP_VALUE, 2)


def rate_with_floor(fat):
    """Calculate a rate using math.floor() for the fat step count."""
    steps = math.floor((fat - STANDARD_FAT) / STEP_SIZE)
    return round(BASE_RATE + steps * FAT_STEP_VALUE, 2)


def payout(litres, fat, snf):
    """Calculate the payment rounded to two decimal places."""
    return round(litres * rate_with_round(fat, snf), 2)


# Normal payment examples
print("NORMAL PAYMENT EXAMPLES")
for litres, fat, snf in [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3),
]:
    print(
        f"{litres:5} L  fat {fat}  snf {snf}"
        f"  rate {rate_with_round(fat, snf):6.2f}"
        f"  pay {payout(litres, fat, snf):8.2f}"
    )

# Floating-point surprises
print("\nUNEXPECTED EXPRESSIONS")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

# Operator precedence
print("\nOPERATOR PRECEDENCE")
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)

# Compare step-count methods for values above and below standard fat
print("\nSTEP COUNT COMPARISON")
for fat in (4.2, 3.1):
    raw_steps = (fat - STANDARD_FAT) / STEP_SIZE
    print(f"\nFat = {fat}, raw steps = {raw_steps}")
    print("round() rate:", rate_with_round(fat, STANDARD_SNF))
    print("int() rate:", rate_with_int(fat))
    print("math.floor() rate:", rate_with_floor(fat))

# Chained comparison and Boolean operators
fat = 4.2
snf = 8.7
valid = 2.0 <= fat <= 7.0 and snf >= 0
print("\nVALIDATION")
print("Fat and SNF valid:", valid)
