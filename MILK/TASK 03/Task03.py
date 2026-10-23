
"""Task 3: Choose variables and name the constants."""

# Named constants for the milk co-operative rate card
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_SIZE = 0.1
SNF_STEP_SIZE = 0.1
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
MIN_FAT = 2.0
MAX_FAT = 7.0
MIN_SNF = 0.0


def rate_per_litre(fat, snf):
    """Calculate the milk rate using the named constants."""
    fat_steps = round((fat - STANDARD_FAT) / FAT_STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / SNF_STEP_SIZE)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


# Demonstrate constants and a rate calculation
print("Base rate:", BASE_RATE)
print("Fat limits:", MIN_FAT, "to", MAX_FAT)
print("Rate for fat 4.2 and SNF 8.7:", rate_per_litre(4.2, 8.7))

# Python variables can refer to values of different types
sample = 10
print("Before reassignment:", sample, type(sample).__name__)

sample = "ten"
print("After reassignment:", sample, type(sample).__name__)

# Multiple assignment and swapping
a, b = 10, 20
a, b = b, a
print("After swapping:", a, b)

# Alternative design: store rate values in a dictionary
RATE_CARD = {
    "base": 30.00,
    "fat": 0.40,
    "snf": 0.30,
}
print("Dictionary rate card:", RATE_CARD)
