import unittest

from hello import greet, greet_name


class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_greet_name(self):
        self.assertEqual(greet_name("Pratik"), "Hello, Pratik!")

    def test_greet_name_trims_whitespace(self):
        self.assertEqual(greet_name("  OpenClaw  "), "Hello, OpenClaw!")

    def test_greet_name_empty_falls_back_to_default(self):
        self.assertEqual(greet_name("   "), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
