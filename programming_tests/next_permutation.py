from typing import List

# paste solution method definition here

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        smallest_swap = None
        smallest_replacement = None
        for index, item in enumerate(nums):
            if index < len(nums) - 1 and item < nums[index + 1]:
                smallest_swap = index
                smallest_replacement = index + 1
            elif smallest_swap is not None and nums[smallest_swap] < item < nums[smallest_replacement]:
                smallest_replacement = index

        if smallest_swap is None:
            nums = sorted(nums)
        else:
            temp_item = nums[smallest_swap]
            nums[smallest_swap] = nums[smallest_replacement]
            nums[smallest_replacement] = temp_item
            nums = nums[:smallest_swap + 1] + sorted(nums[smallest_swap + 1:])
        return nums
# test url: https://leetcode.com/problems/next-permutation/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [[1,2,3]], self.s.nextPermutation, [1,3,2])

    def test_2(self):
        compare(self, [[3,2,1]], self.s.nextPermutation, [1,2,3])
    
    def test_4(self):
        compare(self, [[1,3,2]], self.s.nextPermutation, [2,1,3])
    
        