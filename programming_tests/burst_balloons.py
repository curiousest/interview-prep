from typing import Tuple
from functools import lru_cache

# paste solution method definition here
class Solution:

    @staticmethod
    def pop_value(nums, i):
        left = nums[i-1] if i > 0 else 1
        right = nums[i+1] if i < len(nums) - 1 else 1
        return nums[i] * left * right

    @lru_cache(maxsize=None)
    def maxCoins(self, nums: Tuple[int]) -> int:
        if len(nums) == 0:
            return 0
        return max(self.maxCoins(nums[:i] + nums[i+1:]) + Solution.pop_value(nums, i)
                   for i in range(len(nums)))

# test url: https://leetcode.com/problems/burst-balloons/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [(3,1,5,8)], self.s.maxCoins, 167)

    @unittest.skip
    def test_2(self):
        compare(self, [], self.s.maxCoins, 0)