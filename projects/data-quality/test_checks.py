"""Tests run without third-party dependencies."""
import unittest
from pathlib import Path
from check_data import validate

ROOT = Path(__file__).parent

class ValidationTests(unittest.TestCase):
    def test_clean_file_passes(self):
        errors, revenue = validate(ROOT / "data" / "orders_clean.csv")
        self.assertEqual(errors, [])
        self.assertEqual(revenue, 360)

    def test_bad_file_is_rejected(self):
        errors, _ = validate(ROOT / "data" / "orders_problematic.csv")
        self.assertGreaterEqual(len(errors), 3)
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("unknown customer" in error for error in errors))
        self.assertTrue(any("non-numeric" in error for error in errors))

if __name__ == "__main__":
    unittest.main()
