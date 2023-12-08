import unittest
from my_arithmetic_dchapart import pgcd

class TestPGCD(unittest.TestCase):
    def test_pgcd(self):
        self.assertEqual(pgcd(2, 4), 2)
        self.assertEqual(pgcd(4, 2), 2)
        self.assertEqual(pgcd(2, 3), 1)
        self.assertEqual(pgcd(3, 2), 1)
        self.assertEqual(pgcd(3, 3), 3)
        self.assertEqual(pgcd(3, 0), 3)
        self.assertEqual(pgcd(0, 3), 3)
        self.assertEqual(pgcd(0, 0), 0)
        self.assertEqual(pgcd(1, 0), 1)
        self.assertEqual(pgcd(0, 1), 1)
        self.assertEqual(pgcd(1, 1), 1)
        self.assertEqual(pgcd(1, 2), 1)


if __name__ == '__main__':
    unittest.main()

