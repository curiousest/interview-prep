from typing import List
from functools import lru_cache

# paste solution method definition here

@lru_cache(maxsize=None)
def sets_are_equal(s1, s2):
    return set(s1) == set(s2)

@lru_cache(maxsize=None)
def is_scrambled(s1, s2):
    print("Scrambled: ", s1, s2)
    if set(s1) != set(s2):
        return False
    elif len(s1) == 1:
        return True
    middle = len(s1) // 2
    splits = []
    if len(s1) % 2 == 0:
        splits.append(((s1[:middle], s2[:middle]), (s1[middle:], s2[middle:])))
        splits.append(((s1[:middle], s2[middle:]), (s1[middle:], s2[:middle])))
    else:
        splits.append(((s1[:middle], s2[:middle]), (s1[middle:], s2[middle:])))
        splits.append(((s1[:middle+1], s2[middle:]), (s1[middle:], s2[:middle+1])))
        splits.append(((s1[:middle+1], s2[:middle+1]), (s1[middle+1:], s2[middle+1:])))
        splits.append(((s1[:middle], s2[middle+1:]), (s1[middle:], s2[:middle+1])))
    print("Splits: ")
    for split in splits: print(split)
    for split in splits:
        children_are_equal_sets = sets_are_equal(*split[0]) and sets_are_equal(*split[1])
        if children_are_equal_sets and is_scrambled(*split[0]) and is_scrambled(*split[1]):
            return True
    return False

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return is_scrambled(s1, s2)
        

# test url: https://leetcode.com/problems/scramble-string/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
    @unittest.skip
    def test_1(self):
        compare(self, ['great', 'rgeat'], self.s.isScramble, True)

    @unittest.skip
    def test_2(self):
        compare(self, ['abcde', 'caebd'], self.s.isScramble, False)
    @unittest.skip
    def test_3(self):
        compare(self, ['abb', 'bba'], self.s.isScramble, True)
    
    def test_4(self):
        compare(self, ['abc', 'cab'], self.s.isScramble, True)
    