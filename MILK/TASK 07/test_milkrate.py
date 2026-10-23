
"""Test the milk rate module using different import styles."""

import milkrate
from milkrate import payout
import milkrate as mr


def main():
    """Demonstrate module imports and call payout()."""

    print("METHOD 1: import milkrate")
    print("Rate:", milkrate.rate_per_litre(4.2, 8.7))
    print("Payment:", milkrate.payout(8.5, 4.2, 8.7))

    print("\nMETHOD 2: from milkrate import payout")
    print("Payment:", payout(10, 3.5, 8.5))

    print("\nMETHOD 3: import milkrate as mr")
    print("Rate:", mr.rate_per_litre(3.1, 8.3))
    print("Payment:", mr.payout(12, 3.1, 8.3))


if __name__ == "__main__":
    main()
