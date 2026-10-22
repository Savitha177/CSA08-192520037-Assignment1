"""Tests for the milk rate and payout functions."""

from decimal import Decimal
from milkrate import rate_per_litre, payout


def test_standard_milk():
    assert rate_per_litre(3.5, 8.5) == Decimal("30.00")
    assert payout(10, 3.5, 8.5) == Decimal("300.00")


def test_higher_fat_and_snf():
    assert rate_per_litre(4.2, 8.7) == Decimal("33.40")
    assert payout(8.5, 4.2, 8.7) == Decimal("283.90")


def test_lower_fat_and_snf():
    assert rate_per_litre(3.1, 8.3) == Decimal("27.80")
    assert payout(12, 3.1, 8.3) == Decimal("333.60")


def test_zero_litres():
    assert payout(0, 3.5, 8.5) == Decimal("0.00")


def test_negative_litres_rejected():
    try:
        payout(-1, 3.5, 8.5)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative litres should be rejected")


if __name__ == "__main__":
    test_standard_milk()
    test_higher_fat_and_snf()
    test_lower_fat_and_snf()
    test_zero_litres()
    test_negative_litres_rejected()
    print("All milk payment tests passed!")
