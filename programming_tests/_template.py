from typing import List

# paste solution method definition here


# test url: 

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [], self.s.method_name, 0)

    @unittest.skip
    def test_2(self):
        compare(self, [], self.s.method_name, 0)