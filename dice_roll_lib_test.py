import unittest
import os
from dice_roll_lib import *


# The preparation of constants to use in the test case

MY_DIR = os.path.dirname(os.path.realpath(__file__))


class TestDiceRoll(unittest.TestCase):
    def test_flip_a_coin(self):
        coin = flip_a_coin()
        ht = 'heads' if coin == 0 else 'tails'
        print(f'coin {coin}, {ht}')
        self.assertTrue( 0 <= coin <= 1)

    def test_roll_d4(self):
        d4 = roll_d4()
        print(f'4-sided {d4}')
        self.assertTrue( 1 <= d4 <= 4)

    def test_roll_d6(self):
        d6 = roll_d6()
        print(f'6-sided {d6}')
        self.assertTrue( 1 <= d6 <= 6)

    def test_roll_d8(self):
        d8 = roll_d8()
        print(f'8-sided {d8}')
        self.assertTrue( 1 <= d8 <= 8)

    def test_roll_d10(self):
        d10 = roll_d10()
        print(f'10-sided {d10}')
        self.assertTrue( 1 <= d10 <= 10)

    def test_roll_d12(self):
        d12 = roll_d12()
        print(f'12-sided {d12}')
        self.assertTrue( 1 <= d12 <= 12)

    def test_roll_n_sided_die(self):
        n = 10
        dn = roll_n_sided_die(n)
        print(f'{n}-sided {dn}')
        self.assertTrue( 1 <= dn <= n)

    def test_roll_multiple_n_sided_dice(self):
        number_of_dice = 3
        n = 20
        sum = roll_multiple_n_sided_dice(number_of_dice, n)
        print(f'{number_of_dice} {n}-sided sums to {sum}')
        self.assertTrue( number_of_dice <= sum <= number_of_dice*n )


if __name__ == '__main__':
    unittest.main()
