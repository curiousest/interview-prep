from typing import List

# paste solution method definition here
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        sorted_nums = sorted(nums)
        return max([sorted_nums[i+1] - sorted_nums[i] for i in range(len(nums) - 1)])

# test url: https://leetcode.com/problems/maximum-gap/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [[3,6,9,1]], self.s.maximumGap, 3)

    def test_2(self):
        compare(self, [[10]], self.s.maximumGap, 0)