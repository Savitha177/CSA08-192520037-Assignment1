
import unittest
from decimal import Decimal

from task09_calculator import (
    rate_per_litre,
    payout,
    validate_entry,
    to_decimal,
)


class TestMilkCalculator(unittest.TestCase):

    def test_standard_rate_and_payment(self):
        rate = rate_per_litre(Decimal("3.5"), Decimal("8.5"))
        self.assertEqual(rate, Decimal("30.00"))
        self.assertEqual(
            payout(Decimal("10"), rate),
            Decimal("300.00"),
        )

    def test_higher_fat_and_snf(self):
        rate = rate_per_litre(Decimal("4.2"), Decimal("8.7"))
        self.assertEqual(rate, Decimal("33.40"))
        self.assertEqual(
            payout(Decimal("8.5"), rate),
            Decimal("283.90"),
        )

    def test_lower_fat_and_snf(self):
        rate = rate_per_litre(Decimal("3.1"), Decimal("8.3"))
        self.assertEqual(rate, Decimal("27.80"))
        self.assertEqual(
            payout(Decimal("12"), rate),
            Decimal("333.60"),
        )

    def test_negative_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_entry(
                Decimal("-1"),
                Decimal("3.5"),
                Decimal("8.5"),
            )

    def test_fat_below_minimum_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_entry(
                Decimal("5"),
                Decimal("1.5"),
                Decimal("8.5"),
            )

    def test_fat_above_maximum_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_entry(
                Decimal("5"),
                Decimal("7.1"),
                Decimal("8.5"),
            )

    def test_negative_snf_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_entry(
                Decimal("5"),
                Decimal("3.5"),
                Decimal("-1"),
            )

    def test_comma_decimal_input(self):
        self.assertEqual(to_decimal("8,5"), Decimal("8.5"))

    def test_whitespace_input(self):
        self.assertEqual(to_decimal(" 8.5 "), Decimal("8.5"))


if __name__ == "__main__":
    unittest.main()
