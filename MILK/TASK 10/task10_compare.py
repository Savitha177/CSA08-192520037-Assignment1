
from decimal import Decimal
from time import perf_counter
import sys

# Task 10: Compare float and Decimal

# 1,000 payments of Rs 33.40 and three adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3

REPEATS = 1000


def total_float(items):
    total = 0.0

    for amount in items:
        total += float(amount)

    return total


def total_decimal(items):
    total = Decimal("0.00")

    for amount in items:
        total += Decimal(amount)

    return total


# Calculate totals
float_result = total_float(payments)
decimal_result = total_decimal(payments)

print("MILK CO-OPERATIVE: FLOAT vs DECIMAL")
print("-" * 45)
print("Number of payments:", len(payments))
print(f"Float total:   Rs {float_result:.2f}")
print(f"Decimal total: Rs {decimal_result:.2f}")
print()
print("Float exact representation:", repr(float_result))
print("Decimal exact result:", decimal_result)
print()

# Measure execution time
start = perf_counter()
for _ in range(REPEATS):
    total_float(payments)
float_time = perf_counter() - start

start = perf_counter()
for _ in range(REPEATS):
    total_decimal(payments)
decimal_time = perf_counter() - start

print("TIMING RESULTS")
print("-" * 45)
print("Repeats per method:", REPEATS)
print(f"Float time:   {float_time:.6f} seconds")
print(f"Decimal time: {decimal_time:.6f} seconds")

if float_time > 0:
    print(f"Decimal / float time ratio: {decimal_time / float_time:.2f}x")

print()
print("MEMORY SIZE OF ONE VALUE")
print("-" * 45)
print("float 33.40:", sys.getsizeof(33.40), "bytes")
print('Decimal("33.40"):', sys.getsizeof(Decimal("33.40")), "bytes")
