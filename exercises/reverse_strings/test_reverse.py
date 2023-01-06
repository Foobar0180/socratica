import unittest

from reverse import reverse_string


class TestReverse(unittest.TestCase):
    def test_reversed(self):
        res = reverse_string("Black cat")

        self.assertEqual(res, "tac kcalB")


if __name__ == '__main__':
    unittest.main()
