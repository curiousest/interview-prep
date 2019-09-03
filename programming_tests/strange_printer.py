from typing import List
from functools import lru_cache

@lru_cache(maxsize=None)
def recursive_explore(s: str):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    
    chosen_character = s[0]
    if s[0] != s[-1] and s.count(s[0]) < s.count(s[-1]):
        chosen_character = s[-1]
    
    return 1 + sum(recursive_explore(substring) for substring in s.split(chosen_character))
    
# paste solution method definition here
class Solution:

    def strangePrinter(self, s: str) -> int:
        return recursive_explore(s)

# test url: https://leetcode.com/problems/strange-printer/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, ["aaabbb"], self.s.strangePrinter, 2)

    def test_2(self):
        compare(self, ["aba"], self.s.strangePrinter, 2)

    def test_3(self):
        compare(self, ["abcabc"], self.s.strangePrinter, 5)

    def test_4(self):
        compare(self, ["ababc"], self.s.strangePrinter, 4)

    def test_5(self):
        compare(self, ["tbgtgb"], self.s.strangePrinter, 4)