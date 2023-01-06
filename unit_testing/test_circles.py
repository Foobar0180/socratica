import unittest
from circles import calc_area
from math import pi


class TestCircleArea(unittest.TestCase):

    def test_ShouldReturnAreaWhenRadiusIsValid(self):
        # Test areas where radius >= 0
        self.assertAlmostEqual(calc_area(1), pi)
        self.assertAlmostEqual(calc_area(0), 0)
        self.assertAlmostEqual(calc_area(2.1), pi * 2.1**2)

    def test_ShouldRaiseValueErrorWhenRadiusLessThanZero(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, calc_area, -2)

    def test_ShouldRaiseTypeErrorWhenRadiusNotFloatOrInt(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, calc_area, 3+5j)
        self.assertRaises(TypeError, calc_area, True)
        self.assertRaises(TypeError, calc_area, "radius")
