
"""Task 5: Read input and convert types for milk payment."""

BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STEP_SIZE = 0.1


def read_number(prompt):
    """Read a number from the user and return it as a float."""
    text = input(prompt).strip()

    # Allow decimal comma input such as 8,5 by converting it to 8.5.
    text = text.replace(",", ".")

    try:
        return float(text)
    except ValueError:
        print("Invalid input. Please enter a number, for example 8.5.")
        return None


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre using fat and SNF."""
    fat_steps = round((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / STEP_SIZE)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the payment for the supplied quantity of milk."""
    return round(litres * rate_per_litre(fat, snf), 2)


def main():
    """Read, validate, calculate, and display one milk payment."""
    litres = read_number("Enter milk quantity in litres: ")
    if litres is None:
        return

    fat = read_number("Enter fat percentage (2.0 to 7.0): ")
    if fat is None:
        return

    snf = read_number("Enter SNF percentage (0 or above): ")
    if snf is None:
        return

    if litres < 0:
        print("Invalid quantity. Litres cannot be negative.")
        return

    if not 2.0 <= fat <= 7.0:
        print("Invalid fat percentage. Enter a value from 2.0 to 7.0.")
        return

    if snf < 0:
        print("Invalid SNF percentage. SNF cannot be negative.")
        return

    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)

    print("\n--- Milk Payment Receipt ---")
    print(f"Quantity       : {litres:8.2f} litres")
    print(f"Fat percentage : {fat:8.1f}%")
    print(f"SNF percentage : {snf:8.1f}%")
    print(f"Rate per litre : Rs {rate:8.2f}")
    print(f"Total payment  : Rs {amount:8.2f}")


if __name__ == "__main__":
    main()
