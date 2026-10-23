
from decimal import Decimal, ROUND_HALF_UP


# Original rate card
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
NORMAL_BASE_RATE = Decimal("30.00")
NORMAL_FAT_STEP = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

# New seasonal requirements
SUMMER_BASE_RATE = Decimal("32.00")
SUMMER_FAT_STEP = Decimal("0.45")

BONUS_THRESHOLD = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
STEP_SIZE = Decimal("0.1")
MONEY_PLACES = Decimal("0.01")


def select_rate_card(season):
    """Return the rate card for the selected season."""
    season = season.strip().lower()

    if season in ("april", "may", "june", "summer"):
        return {
            "base_rate": SUMMER_BASE_RATE,
            "fat_step": SUMMER_FAT_STEP,
            "snf_step": SNF_STEP_VALUE,
        }

    if season in (
        "january", "february", "march",
        "july", "august", "september",
        "october", "november", "december",
        "normal", "other"
    ):
        return {
            "base_rate": NORMAL_BASE_RATE,
            "fat_step": NORMAL_FAT_STEP,
            "snf_step": SNF_STEP_VALUE,
        }

    raise ValueError("Enter a valid month or 'summer'/'normal'.")


def rate_per_litre(fat, snf, season):
    """Calculate the rate using the selected seasonal rate card."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    card = select_rate_card(season)

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0% and 7.0%.")

    if snf < 0:
        raise ValueError("SNF cannot be negative.")

    fat_steps = (fat - STANDARD_FAT) / STEP_SIZE
    snf_steps = (snf - STANDARD_SNF) / STEP_SIZE

    rate = (
        card["base_rate"]
        + fat_steps * card["fat_step"]
        + snf_steps * card["snf_step"]
    )

    return rate.quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)


def payout(litres, rate):
    """Calculate the payment for one milk delivery."""
    litres = Decimal(str(litres))
    rate = Decimal(str(rate))

    if litres < 0:
        raise ValueError("Litres cannot be negative.")

    return (litres * rate).quantize(
        MONEY_PLACES, rounding=ROUND_HALF_UP
    )


def bonus_for_ten_days(total_litres):
    """Give the bonus only when ten-day quantity exceeds 500 litres."""
    total_litres = Decimal(str(total_litres))

    if total_litres > BONUS_THRESHOLD:
        return (total_litres * BONUS_PER_LITRE).quantize(
            MONEY_PLACES, rounding=ROUND_HALF_UP
        )

    return Decimal("0.00")


def calculate_ten_day_payment(deliveries, season):
    """
    Each delivery is a tuple: (litres, fat, snf).
    Returns total litres, normal payment, bonus and final payment.
    """
    total_litres = Decimal("0")
    normal_payment = Decimal("0")

    for litres, fat, snf in deliveries:
        litres = Decimal(str(litres))

        if litres < 0:
            raise ValueError("Litres cannot be negative.")

        rate = rate_per_litre(fat, snf, season)
        total_litres += litres
        normal_payment += payout(litres, rate)

    bonus = bonus_for_ten_days(total_litres)
    final_payment = (normal_payment + bonus).quantize(
        MONEY_PLACES, rounding=ROUND_HALF_UP
    )

    return {
        "total_litres": total_litres,
        "normal_payment": normal_payment,
        "bonus": bonus,
        "final_payment": final_payment,
    }


def main():
    print("MILK CO-OPERATIVE - TASK 12")
    print("Seasonal Rates and Ten-Day Bonus")
    print("-" * 38)

    season = input(
        "Enter month (April-June for seasonal rates): "
    ).strip()

    try:
        card = select_rate_card(season)
    except ValueError as error:
        print("Invalid season:", error)
        return

    print(f"Base rate: Rs {card['base_rate']}")
    print(f"Fat step value: Rs {card['fat_step']}")
    print(f"SNF step value: Rs {card['snf_step']}")
    print("Enter a blank farmer ID to finish.")

    farmers = {}

    while True:
        farmer_id = input("\nFarmer ID: ").strip()

        if not farmer_id:
            break

        try:
            litres = Decimal(
                input("Milk quantity in litres: ").strip().replace(",", ".")
            )
            fat = Decimal(
                input("Fat percentage: ").strip().replace(",", ".")
            )
            snf = Decimal(
                input("SNF percentage: ").strip().replace(",", ".")
            )

            rate = rate_per_litre(fat, snf, season)
            payment = payout(litres, rate)

            if farmer_id not in farmers:
                farmers[farmer_id] = {
                    "litres": Decimal("0"),
                    "normal_payment": Decimal("0"),
                }

            farmers[farmer_id]["litres"] += litres
            farmers[farmer_id]["normal_payment"] += payment

            print(f"Rate per litre: Rs {rate}")
            print(f"Delivery payment: Rs {payment}")

        except (ValueError, ArithmeticError) as error:
            print("Invalid entry:", error)
            print("This entry was not added. Please try again.")

    print("\nTEN-DAY PAYMENT SUMMARY")
    print("-" * 38)

    centre_total = Decimal("0")

    for farmer_id, data in farmers.items():
        litres = data["litres"]
        normal = data["normal_payment"]
        bonus = bonus_for_ten_days(litres)
        final = (normal + bonus).quantize(
            MONEY_PLACES, rounding=ROUND_HALF_UP
        )

        centre_total += final

        print(f"Farmer ID: {farmer_id}")
        print(f"Total litres: {litres}")
        print(f"Normal payment: Rs {normal:.2f}")
        print(f"Bonus: Rs {bonus:.2f}")
        print(f"Final payment: Rs {final:.2f}")
        print("-" * 25)

    print(f"Centre total payment: Rs {centre_total:.2f}")


if __name__ == "__main__":
    main()
