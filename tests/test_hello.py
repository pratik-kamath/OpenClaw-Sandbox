import unittest
from datetime import datetime, UTC
from unittest.mock import patch

from hello import current_time_utc, greet, greet_name


class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_name(self):
        self.assertEqual(greet_name("Pratik"), "Hello, Pratik!")

    def test_greet_name_trims_whitespace(self):
        self.assertEqual(greet_name("  OpenClaw  "), "Hello, OpenClaw!")

    def test_greet_name_empty_falls_back_to_default(self):
        self.assertEqual(greet_name("   "), "Hello, World!")

    def test_current_time_utc(self):
        fixed_time = datetime(2026, 3, 5, 12, 34, tzinfo=UTC)
        with patch("hello.datetime") as mock_datetime:
            mock_datetime.now.return_value = fixed_time
            self.assertEqual(current_time_utc(), "Hello, World! It is 12:34 UTC")


if __name__ == "__main__":
    unittest.main()
