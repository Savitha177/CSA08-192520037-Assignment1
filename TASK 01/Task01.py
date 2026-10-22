"""Interactive milk co-operative payment calculator for Task 01."""

from decimal import Decimal, InvalidOperation

from milkrate import payout, rate_per_litre

# Constants used to validate milk entries
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")


def main():
    """Collect one milk entry, validate it, and show the payment."""
    farmer_id = input("Enter farmer ID: ").strip()

    try:
        litres = Decimal(input("Enter litres of milk: ").strip())
        fat = Decimal(input("Enter fat percentage: ").strip())
        snf = Decimal(input("Enter SNF percentage: ").strip())
    except InvalidOperation:
        print("Invalid input: litres, fat, and SNF must be numbers.")
        return

    shift = input("Enter shift (Morning/Evening): ").strip().title()

    # Reject special Decimal values such as NaN or Infinity before comparisons.
    if not all(value.is_finite() for value in (litres, fat, snf)):
        print("Invalid input: litres, fat, and SNF must be finite numbers.")
        return

    # Validate before doing any calculations.
    errors = []

    if not farmer_id:
        errors.append("Farmer ID cannot be empty.")
    if litres < 0:
        errors.append("Litres cannot be negative.")
    if not (MIN_FAT <= fat <= MAX_FAT):
        errors.append("Fat must be between 2.0% and 7.0%.")
    if snf < 0:
        errors.append("SNF cannot be negative.")
    if shift not in ("Morning", "Evening"):
        errors.append("Shift must be Morning or Evening.")

    if errors:
        print("\nInvalid milk entry:")
        for error in errors:
            print("-", error)
        print("No payment was calculated.")
        return

    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)

    print("\nMilk entry is valid.")
    print("Farmer ID:", farmer_id)
    print("Litres:", litres)
    print("Fat:", fat)
    print("SNF:", snf)
    print("Shift:", shift)
    print("Rate per litre: Rs", rate)
    print("Payment: Rs", amount)


if __name__ == "__main__":
    main()
