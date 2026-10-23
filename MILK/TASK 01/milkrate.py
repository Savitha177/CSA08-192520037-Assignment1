"""Rate card and payment functions for the milk co-operative."""

from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
MONEY_PLACES = Decimal("0.01")


def _as_decimal(value, name):
    """Convert a number-like value to Decimal with a useful error."""
    try:
        result = Decimal(str(value))
    except Exception as exc:
        raise ValueError(f"{name} must be a number.") from exc
    if not result.is_finite():
        raise ValueError(f"{name} must be a finite number.")
    return result


def rate_per_litre(fat, snf):
    """Return the rate per litre based on fat and SNF percentages."""
    fat = _as_decimal(fat, "Fat")
    snf = _as_decimal(snf, "SNF")

    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return rate.quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf):
    """Return the total payment rounded to two decimal places."""
    litres = _as_decimal(litres, "Litres")
    if litres < 0:
        raise ValueError("Litres cannot be negative.")

    rate = rate_per_litre(fat, snf)
    return (litres * rate).quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    examples = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
    ]

    for litres, fat, snf in examples:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(
            f"{litres:5} L  fat {fat}  SNF {snf}"
            f"  rate {rate:6.2f}  pay {amount:8.2f}"
        )
