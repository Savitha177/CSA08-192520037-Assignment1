
import unittest
from decimal import Decimal

from task12_calculator import (
    select_rate_card,
    rate_per_litre,
    payout,
    bonus_for_ten_days,
    calculate_ten_day_payment,
)


class TestTask12Calculator(unittest.TestCase):

    def test_normal_season_rate(self):
        self.assertEqual(
            rate_per_litre("3.5", "8.5", "normal"),
            Decimal("30.00")
        )

    def test_summer_season_rate(self):
        self.assertEqual(
            rate_per_litre("3.5", "8.5", "April"),
            Decimal("32.00")
        )

    def test_fat_step_changes_by_season(self):
        self.assertEqual(
            rate_per_litre("4.2", "8.7", "normal"),
            Decimal("33.40")
        )
        self.assertEqual(
            rate_per_litre("4.2", "8.7", "April"),
            Decimal("35.75")
        )

    def test_two_decimal_readings(self):
        self.assertEqual(
            rate_per_litre("3.55", "8.52", "April"),
            Decimal("32.29")
        )

    def test_normal_payout(self):
        self.assertEqual(
            payout("10", "30.00"),
            Decimal("300.00")
        )

    def test_bonus_when_more_than_500_litres(self):
        self.assertEqual(
            bonus_for_ten_days("510"),
            Decimal("255.00")
        )

    def test_no_bonus_at_exactly_500_litres(self):
        self.assertEqual(
            bonus_for_ten_days("500"),
            Decimal("0.00")
        )

    def test_ten_day_final_payment(self):
        result = calculate_ten_day_payment(
            [("510", "3.5", "8.5")],
            "April"
        )
        self.assertEqual(result["total_litres"], Decimal("510"))
        self.assertEqual(result["normal_payment"], Decimal("16320.00"))
        self.assertEqual(result["bonus"], Decimal("255.00"))
        self.assertEqual(result["final_payment"], Decimal("16575.00"))

    def test_invalid_fat(self):
        with self.assertRaises(ValueError):
            rate_per_litre("7.1", "8.5", "April")

    def test_negative_snf(self):
        with self.assertRaises(ValueError):
            rate_per_litre("3.5", "-0.1", "April")

    def test_negative_litres(self):
        with self.assertRaises(ValueError):
            payout("-1", "30.00")

    def test_invalid_season(self):
        with self.assertRaises(ValueError):
            select_rate_card("UnknownMonth")


if __name__ == "__main__":
    unittest.main()
