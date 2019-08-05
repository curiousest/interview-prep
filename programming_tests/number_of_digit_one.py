import math

# paste solution method definition here

class Solution:
    def countDigitOne(self, n: int) -> int:
        count_ones = 0
        significant_digits = math.ceil(math.log10(n))
        first_digit = n // 10 ** (significant_digits - 1)
        print(significant_digits, first_digit)
        for significant_digit in range(significant_digits - 1):
            count_ones += first_digit * 10**(significant_digits - significant_digit - 2)
        if first_digit == 1:
            pass
            
        return count_ones

# test url: https://leetcode.com/problems/number-of-digit-one/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [13], self.s.countDigitOne, 6)

    def test_2(self):
        compare(self, [99], self.s.countDigitOne, 20)