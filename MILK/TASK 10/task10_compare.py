
from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter
import sys

# The assignment requires these three payment counts.
SIZES = (300, 6_000, 150_000)
REPEATS = 3

# Use string values to avoid importing float approximation into Decimal.
PAYMENT_STRINGS = ("33.40", "0.10", "27.80", "12.35", "19.99")


def float_total(values):
    total = 0.0
    for value in values:
        total += float(value)
    return total


def decimal_total(values):
    total = Decimal("0.00")
    for value in values:
        total += Decimal(value)
    return total


def round_money(value):
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def decimal_rounded_each_total(values):
    total = Decimal("0.00")
    for value in values:
        total += round_money(Decimal(value))
    return total


def decimal_round_only_final_total(values):
    total = Decimal("0.00")
    for value in values:
        total += Decimal(value)
    return round_money(total)


def time_function(function, values, repeats=REPEATS):
    start = perf_counter()
    result = None
    for _ in range(repeats):
        result = function(values)
    elapsed = perf_counter() - start
    return result, elapsed


def compare_totals():
    print("FLOAT VS DECIMAL TOTALS")
    print("-" * 72)

    for size in SIZES:
        values = [PAYMENT_STRINGS[i % len(PAYMENT_STRINGS)]
                  for i in range(size)]

        float_result, float_seconds = time_function(float_total, values)
        decimal_result, decimal_seconds = time_function(decimal_total, values)

        print(f"\nNumber of payments: {size:,}")
        print(f"Float total: Rs {float_result:.2f}")
        print(f"Decimal total: Rs {decimal_result:.2f}")
        print(f"Float raw result: {float_result!r}")
        print(f"Decimal exact result: {decimal_result}")
        print(f"Float time ({REPEATS} runs): {float_seconds:.6f} seconds")
        print(f"Decimal time ({REPEATS} runs): {decimal_seconds:.6f} seconds")

        if float_seconds > 0:
            print(f"Decimal / float time ratio: "
                  f"{decimal_seconds / float_seconds:.2f}x")

    print("\nOBJECT SIZE EXAMPLE")
    print(f"float 33.40: {sys.getsizeof(33.40)} bytes")
    print(f'Decimal("33.40"): '
          f'{sys.getsizeof(Decimal("33.40"))} bytes')


def compare_rounding():
    # Deliberately use fractional-paise values to show the policy difference.
    values = ["0.005", "0.005", "0.005"]

    each_total = decimal_rounded_each_total(values)
    final_total = decimal_round_only_final_total(values)

    print("\nROUNDING STRATEGY COMPARISON")
    print("-" * 72)
    print(f"Test payments: {values}")
    print(f"Round each payment, then add: Rs {each_total}")
    print(f"Add exact values, round once: Rs {final_total}")
    print("Use the rounding policy specified by the co-operative.")


def rate_lookup_dictionary():
    # Small example rate card. This demonstrates lookup performance,
    # not a replacement for the full fat/SNF calculation.
    rate_card = {
        (3.5, 8.5): Decimal("30.00"),
        (4.2, 8.7): Decimal("33.40"),
        (3.1, 8.3): Decimal("27.80"),
    }

    keys = list(rate_card.keys())
    lookup_count = 150_000

    start = perf_counter()
    total = Decimal("0.00")
    for i in range(lookup_count):
        total += rate_card[keys[i % len(keys)]]
    elapsed = perf_counter() - start

    print("\nDICTIONARY RATE LOOKUP ALTERNATIVE")
    print("-" * 72)
    print(f"Lookups: {lookup_count:,}")
    print(f"Lookup total (demonstration only): Rs {total}")
    print(f"Dictionary lookup loop time: {elapsed:.6f} seconds")
    print("Expected average dictionary lookup: O(1)")
    print("Building/loading a rate card with k entries: O(k) time/space")


if __name__ == "__main__":
    compare_totals()
    compare_rounding()
    rate_lookup_dictionary()

