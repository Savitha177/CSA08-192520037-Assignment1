
import unittest
import milkrate


class TestMilkRate(unittest.TestCase):

    def test_standard_rate(self):
        self.assertEqual(
            milkrate.rate_per_litre(3.5, 8.5),
            30.00
        )

    def test_high_fat_rate(self):
        self.assertEqual(
            milkrate.rate_per_litre(4.2, 8.7),
            33.40
        )

    def test_low_fat_rate(self):
        self.assertEqual(
            milkrate.rate_per_litre(3.1, 8.3),
            27.80
        )

    def test_standard_payment(self):
        self.assertEqual(
            milkrate.payout(10, 3.5, 8.5),
            300.00
        )


if __name__ == "__main__":
    unittest.main()
