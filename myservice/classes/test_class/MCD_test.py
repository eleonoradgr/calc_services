import myservice.classes.calculator as c
import unittest


class TestMCD(unittest.TestCase):

    def test_MCD_integers_positive(self):
        result = c.MCD(6, 3)
        self.assertEqual(result, 3)

    def test_MCD_integers_positive_prime(self):
        result = c.MCD(7, 3)
        self.assertEqual(result, 1)

    def test_MCD_integers_negative(self):
        result = c.MCD(-6, -2)
        self.assertEqual(result, 2)

    def test_MCD_integers_negative_prime(self):
        result = c.MCD(-7, -2)
        self.assertEqual(result, 1)

    def test_MCD_integers_pos_neg(self):
        result = c.MCD(6, -2)
        self.assertEqual(result, 2)

    def test_MCD_integers_pos_neg2(self):
        result = c.MCD(10, -2)
        self.assertEqual(result, 2)

    def test_MCD_integers_neg_pos(self):
        result = c.MCD(-6, 2)
        self.assertEqual(result, 2)

    def test_MCD_integers_neg_pos2(self):
        result = c.MCD(-10, 5)
        self.assertEqual(result, 5)

    def test_MCD_zero(self):
        result = c.MCD(0, 2)
        self.assertEqual(result, 2)

    def test_MCD_zero2(self):
        result = c.MCD(2, 0)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
