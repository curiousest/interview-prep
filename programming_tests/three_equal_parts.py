from typing import List

# paste solution method definition here
class Solution:
    def add_new_to_explore(self, next_item):
        if next_item not in self.explored:
            self.stack.append(next_item)
            self.explored.add(next_item)

    def threeEqualParts(self, A: List[int]) -> List[int]:
        a = ''.join(str(i) for i in A)
        i = 0
        j = len(a) - 1
        start = (i, j)
        self.stack = [start]
        self.explored = set(start)
        while self.stack:
            i, j = self.stack.pop()
            if j - i == 1: continue
            print(i, j)
            bottom = int(a[:i+1])
            middle = int(a[i+1:j])
            top = int(a[j:])
            print(top, middle, bottom)
            if bottom == middle == top:
                return [i, j]
            
            if bottom > middle and i > 0:
                self.add_new_to_explore((i-1, j))
            elif bottom < middle and j-i > 1:
                self.add_new_to_explore((i+1, j))
            
            if middle > top and j-i > 1:
                self.add_new_to_explore((i, j-1))
            elif middle < top and j < len(a) - 1:
                self.add_new_to_explore((i, j+1))

            if bottom > top:
                if i > 0:
                    self.add_new_to_explore((i-1, j))
                if j - i > 1:
                    self.add_new_to_explore((i, j-1))
            elif bottom < top:
                if j < len(a) - 1:
                    self.add_new_to_explore((i, j+1))
                if j - i > 1:
                    self.add_new_to_explore((i + 1, j))
        return [-1, -1]

            

            
# test url: https://leetcode.com/problems/three-equal-parts/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

#    def test_1(self):
#        compare(self, [[1,0,1,0,1]], self.s.threeEqualParts, [0, 3])

#    def test_2(self):
#        compare(self, [[1,1,0,1,1]], self.s.threeEqualParts, [-1,-1])
    
    def test_3(self):
        compare(self, [[1,0,1,1,0]], self.s.threeEqualParts, [0,3])
            

    #  [1,0,0,0,0,0,1,0,0,1]
