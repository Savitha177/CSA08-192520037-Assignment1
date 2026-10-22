
from decimal import Decimal, ROUND_HALF_UP

# Named constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

FAT_STEP_SIZE = Decimal("0.1")
SNF_STEP_SIZE = Decimal("0.1")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
ZERO = Decimal("0")
CENT = Decimal("0.01")


def to_decimal(text):
    """Convert user input to Decimal; accept 8.5 or 8,5."""
    return Decimal(text.strip().replace(",", "."))


def rate_per_litre(fat, snf):
    """Calculate the milk rate from fat and SNF percentages."""
    fat_steps = ((fat - STANDARD_FAT) / FAT_STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    snf_steps = ((snf - STANDARD_SNF) / SNF_STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )

    return rate.quantize(CENT, rounding=ROUND_HALF_UP)


def payout(litres, rate):
    """Calculate a farmer's payment, rounded to the nearest paisa."""
    return (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)


def validate_entry(litres, fat, snf):
    """Reject invalid milk quantity, fat or SNF values."""
    if litres < ZERO:
        raise ValueError("Milk quantity cannot be negative.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0% and 7.0%.")

    if snf < ZERO:
        raise ValueError("SNF cannot be negative.")


def main():
    print("VILLAGE MILK CO-OPERATIVE PAYMENT CALCULATOR")
    print("-" * 45)

    while True:
        try:
            count_text = input("Number of entries to process: ").strip()
            count = int(count_text)

            if count < 0:
                print("Please enter zero or a positive number.")
                continue

            break
        except ValueError:
            print("Please enter a whole number, such as 3.")

    farmer_totals = {}
    centre_total = ZERO

    for entry_number in range(1, count + 1):
        print(f"\nEntry {entry_number}")

        farmer_id = input("Farmer ID: ").strip()

        try:
            if not farmer_id:
                raise ValueError("Farmer ID cannot be empty.")

            litres = to_decimal(input("Milk quantity in litres: "))
            fat = to_decimal(input("Fat percentage: "))
            snf = to_decimal(input("SNF percentage: "))

            validate_entry(litres, fat, snf)

            rate = rate_per_litre(fat, snf)
            amount = payout(litres, rate)

            farmer_totals[farmer_id] = (
                farmer_totals.get(farmer_id, ZERO) + amount
            ).quantize(CENT, rounding=ROUND_HALF_UP)

            centre_total = (centre_total + amount).quantize(
                CENT, rounding=ROUND_HALF_UP
            )

            print(f"Rate per litre: Rs {rate:.2f}")
            print(f"Payment for this entry: Rs {amount:.2f}")

        except (ValueError, ArithmeticError) as error:
            print(f"Entry rejected: {error}")
            print("This entry will be skipped.")

    print("\n" + "=" * 45)
    print("PAYMENT SUMMARY")
    print("-" * 45)

    if farmer_totals:
        for farmer_id, total in sorted(farmer_totals.items()):
            print(f"Farmer {farmer_id}: Rs {total:.2f}")
    else:
        print("No valid farmer entries were recorded.")

    print("-" * 45)
    print(f"Centre total: Rs {centre_total:.2f}")
    print("Note: Totals include valid entries only.")


if __name__ == "__main__":
    main()
