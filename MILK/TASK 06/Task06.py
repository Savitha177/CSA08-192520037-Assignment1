
"""Task 6: Organise the milk payment logic into functions."""

# Global constants: shared rate-card values.
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STEP_SIZE = 0.1


def rate_per_litre(fat, snf):
    """Return the milk rate per litre for the given fat and SNF."""
    fat_steps = round((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / STEP_SIZE)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment for one milk entry."""
    rate = rate_per_litre(fat, snf)
    amount = litres * rate
    return round(amount, 2)


def ten_day_total(entries):
    """Return the total payment for a list of milk entries.

    Each entry is a tuple containing (litres, fat, snf).
    """
    total = 0.0

    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)

    return round(total, 2)


def main():
    """Demonstrate the functions using sample milk entries."""
    # Local variable: it exists inside main().
    examples = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
    ]

    print("INDIVIDUAL MILK PAYMENTS")
    print("-" * 60)

    for litres, fat, snf in examples:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)

        print(
            f"Quantity: {litres:6.2f} L | "
            f"Fat: {fat:4.1f}% | "
            f"SNF: {snf:4.1f}% | "
            f"Rate: Rs {rate:6.2f} | "
            f"Payment: Rs {amount:7.2f}"
        )

    total = ten_day_total(examples)

    print("-" * 60)
    print(f"Total payment for these entries: Rs {total:.2f}")


if __name__ == "__main__":
    main()
