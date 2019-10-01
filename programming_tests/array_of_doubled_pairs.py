from typing import List
from collections import Counter

# paste solution method definition here
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        indexed_items = Counter(A)
        a = list(sorted(item for item in A if item > 0)) + list(sorted([item for item in A if item <= 0], reverse=True))
        for item in a:
            if indexed_items[item] == 0:
                continue
            indexed_items[item] -= 1
            if indexed_items.get(item * 2, 0) > 0:
                indexed_items[item*2] -= 1
            else:
                return False
        return True


# test url: https://leetcode.com/problems/array-of-doubled-pairs/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
    
    def test_1(self):
        compare(self, [[3,1,3,6]], self.s.canReorderDoubled, False)
    
    def test_2(self):
        compare(self, [[2,1,2,6]], self.s.canReorderDoubled, False)
    
    def test_3(self):
        compare(self, [[4,-2,2,-4]], self.s.canReorderDoubled, True)
    
    def test_4(self):
        compare(self, [[1,2,4,16,8,4]], self.s.canReorderDoubled, False)
    
    def test_5(self):
        compare(self, [[-5,-3]], self.s.canReorderDoubled, False)
    