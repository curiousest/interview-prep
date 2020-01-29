from typing import List

# paste solution method definition here

class Solution:
    
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) < 2 or stones[1] != 1:
            return False
        elif len(stones) == 2:
            return True
        paths = [{'last_k': 1, 'stones': stones[1:]}]

        while paths:
            path = paths.pop()
            end = self.nextJump(path['last_k'], path['stones'], paths)
            if end:
                return True
        return False

    def nextJump(self, last_k: int, stones: List[int], paths) -> bool:
        if last_k > 1:
            try:
                k_minus_one = stones.index(stones[0] + last_k - 1)
                if k_minus_one == len(stones) - 1:
                    return True
                paths.append({'last_k': last_k - 1, 'stones': stones[k_minus_one:]})
            except ValueError:
                pass
        try:
            k_again = stones.index(stones[0] + last_k)
            if k_again == len(stones) - 1:
                return True
            paths.append({'last_k': last_k, 'stones': stones[k_again:]})
        except ValueError:
            pass
        try:
            k_plus_one = stones.index(stones[0] + last_k + 1)
            if k_plus_one == len(stones) - 1:
                return True
            paths.append({'last_k': last_k + 1, 'stones': stones[k_plus_one:]})
        except ValueError:
            pass
        return False

        

# test url: https://leetcode.com/problems/frog-jump/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    @unittest.skip
    def test_1(self):
        compare(self, [[0,1,3,5,6,8,12,17]], self.s.canCross, True)

    def test_2(self):
        compare(self, [[0,1,2,3,4,8,9,11]], self.s.canCross, False)