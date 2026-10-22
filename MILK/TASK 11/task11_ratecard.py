import json
from decimal import Decimal
from time import perf_counter
from pathlib import Path

ratecard_path = Path(__file__).with_name("ratecard.json")

start = perf_counter()

with ratecard_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

rate_card = {
    key: Decimal(value)
    for key, value in data.items()
}

elapsed = perf_counter() - start

print("Rate card loaded successfully.")
print("Base rate:", rate_card["base_rate"])
print("Fat step value:", rate_card["fat_step_value"])
print("SNF step value:", rate_card["snf_step_value"])
print(f"JSON loading time: {elapsed:.8f} seconds")
print("Number of rate values:", len(rate_card))