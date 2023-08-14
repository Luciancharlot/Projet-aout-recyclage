import unittest
from Fractions import Fraction


class TestFraction(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)
        self.assertRaises(ValueError, Fraction, 1, "lucian")
        self.assertRaises(ValueError, Fraction, "lucian", 1)
        self.assertRaises(ValueError, Fraction, 1.5, "lucian")
        self.assertRaises(ValueError, Fraction, 1, "lucian")
        self.assertRaises(ValueError, Fraction, 1, 1.5)
        self.assertRaises(ValueError, Fraction, None, 2)
        self.assertRaises(ValueError, Fraction, 1, None)

        self.assertEqual(Fraction(5, 10).numerator, 5)
        self.assertEqual(Fraction(5, 10).denominator, 10)
        self.assertEqual(Fraction(-1, 2).numerator, -1)
        self.assertEqual(Fraction(-1, 2).denominator, 2)
        self.assertEqual(Fraction(-5, -10).numerator, -5)
        self.assertEqual(Fraction(-5, -10).denominator, -10)
        self.assertEqual(Fraction(0, 1).numerator, 0)
        self.assertEqual(Fraction(0, 1).denominator, 1)

    def test_pgcd(self):
        self.assertEqual(Fraction.pgcd(5, 10), 5)
        self.assertEqual(Fraction.pgcd(-5, 10), 5)
        self.assertEqual(Fraction.pgcd(5, -10), -5)

    def test_check_other(self):
        self.assertEqual(Fraction.check_other(Fraction(5, 10)), True)
        self.assertEqual(Fraction.check_other('test'), False)

    def test_str(self):
        self.assertEqual(str(Fraction(5, 10)), "The fraction is 1/2")

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(5, 10).as_mixed_number(), "Mixed number : 0 and 5/10")
        self.assertEqual(Fraction(31, 10).as_mixed_number(), "Mixed number : 3 and 1/10")
        self.assertEqual(Fraction(5, 1).as_mixed_number(), "Mixed number : 5")
        self.assertEqual(Fraction(-5, 1).as_mixed_number(), "Mixed number : -5")
        self.assertEqual(Fraction(5, -1).as_mixed_number(), "Mixed number : -5")

    def test_add(self):
        with self.assertRaises(TypeError):
            Fraction(5, 10) + "pas un objet fraction"
        self.assertEqual(Fraction(5, 10) + (Fraction(5, 10)), Fraction(1, 1))
        self.assertEqual(Fraction(5, 10) + (Fraction(-5, 10)), Fraction(0, 1))
        self.assertEqual(Fraction(5, 10) + (Fraction(5, -10)), Fraction(0, 1))
        self.assertEqual(Fraction(-5, 10) + (Fraction(-5, 10)), Fraction(-1, 1))
        self.assertEqual(Fraction(5, -10) + (Fraction(5, -10)), Fraction(-1, 1))

    def test_sub(self):
        with self.assertRaises(TypeError):
            Fraction(5, 10) - "pas un objet fraction"
        self.assertEqual(Fraction(5, 10) - (Fraction(5, 10)), Fraction(0, 1))
        self.assertEqual(Fraction(5, 10) - (Fraction(-5, 10)), Fraction(1, 1))
        self.assertEqual(Fraction(-5, 10) - (Fraction(-5, 10)), Fraction(0, 1))
        self.assertEqual(Fraction(5, -10) - (Fraction(5, -10)), Fraction(0, 1))

    def test_mul(self):
        with self.assertRaises(TypeError):
            Fraction(5, 10) * "pas un objet fraction"
        self.assertEqual(Fraction(5, 10) * (Fraction(5, 10)), Fraction(1, 4))
        self.assertEqual(Fraction(-5, 10) * (Fraction(5, 10)), Fraction(-1, 4))
        self.assertEqual(Fraction(-5, 10) * (Fraction(-5, 10)), Fraction(1, 4))
        self.assertEqual(Fraction(5, -10) * (Fraction(5, -10)), Fraction(1, 4))

    def test_true_div(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(5, 10) / Fraction(0, 1)
        with self.assertRaises(TypeError):
            Fraction(5, 10) / "pas un objet fraction"
        self.assertEqual(Fraction(5, 10) / (Fraction(5, 10)), Fraction(1, 1))
        self.assertEqual(Fraction(-5, 10) / (Fraction(5, 10)), Fraction(-1, 1))
        self.assertEqual(Fraction(5, -10) / (Fraction(5, 10)), Fraction(-1, 1))
        self.assertEqual(Fraction(-5, 10) / (Fraction(5, -10)), Fraction(1, 1))
        self.assertEqual(Fraction(5, -10) / (Fraction(-5, 10)), Fraction(1, 1))
        self.assertEqual(Fraction(5, -10) / (Fraction(5, -10)), Fraction(1, 1))
        self.assertEqual(Fraction(4, 1) / (Fraction(2, 1)), Fraction(2, 1))
        self.assertEqual(Fraction(4, 1) / (Fraction(2, 1)), Fraction(2, 1))

    def test_pow(self):
        with self.assertRaises(TypeError):
            Fraction(5, 10) ** "pas un objet fraction"
        self.assertEqual(Fraction(4, 1) ** (Fraction(2, 1)), Fraction(16, 1))
        self.assertEqual(Fraction(-4, 1) ** (Fraction(2, 1)), Fraction(16, 1))

    def test__eq(self):
        with self.assertRaises(TypeError):
            Fraction(5, 10) == "pas un objet fraction"
        self.assertEqual(Fraction(4, 1) == (Fraction(4, 1)), True)
        self.assertEqual(Fraction(4, 1) == (Fraction(2, 1)), False)

    def test_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(-1, 2)), -0.5)

    def test_is_zero(self):
        self.assertEqual(Fraction(0, 12).is_zero(), True)
        self.assertEqual(Fraction(16, 12).is_zero(), False)
        self.assertEqual(Fraction(-16, 12).is_zero(), False)
        self.assertEqual(Fraction(16, -12).is_zero(), False)

    def test_is_integer(self):
        self.assertEqual(Fraction(8, 4).is_integer(), True)
        self.assertEqual(Fraction(-24, 12).is_integer(), True)
        self.assertEqual(Fraction(3, 12).is_integer(), False)
        self.assertEqual(Fraction(-3, 12).is_integer(), False)

    def test_is_proper(self):
        self.assertEqual(Fraction(2, 12).is_proper(), True)
        self.assertEqual(Fraction(49, 12).is_proper(), False)
        self.assertEqual(Fraction(-49, 12).is_proper(), False)

    def test_is_unit(self):
        self.assertEqual(Fraction(2, 12).is_unit(), True)
        self.assertEqual(Fraction(-2, 12).is_unit(), False)
        self.assertEqual(Fraction(2, -12).is_unit(), False)
        self.assertEqual(Fraction(8, 12).is_unit(), False)

    def test_is_adjacent(self):
        self.assertEqual(Fraction(1, 2).is_adjacent_to(Fraction(2, 2)), True)
        self.assertEqual(Fraction(2, 2).is_adjacent_to(Fraction(1, 2)), True)
        self.assertEqual(Fraction(-1, 2).is_adjacent_to(Fraction(-2, 2)), True)
        self.assertEqual(Fraction(2, -2).is_adjacent_to(Fraction(1, -2)), True)
        self.assertEqual(Fraction(1, 2).is_adjacent_to(Fraction(3, 2)), False)


if __name__ == '__main__':
    unittest.main()
