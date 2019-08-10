from typing import List

# paste solution method definition here

class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_size = 0
        for row_index, row in enumerate(matrix):
            for col_index, cell in enumerate(row):
                max_size = max(max_size, self.rectangle_size(matrix, row_index, col_index))
        return max_size

    def rectangle_size(self, matrix, row_index, col_index):
        
        if matrix[row_index][col_index] == "0":
            return 0

        # find max column for this rectangle
        col = col_index
        while col + 1 < len(matrix[0]) and matrix[row_index][col + 1] != "0":
            #print(row_index, col_index, matrix[row_index][col + 1])
            col += 1

        max_rectangle_size = col - col_index + 1
       
        max_col = col
        row = row_index
        while row + 1 < len(matrix) and matrix[row + 1][col_index] != "0":
            row += 1
            col = col_index
            # start with current max col
            # find first cell in next row that's a 0
            while col + 1 <= max_col and matrix[row][col + 1] != "0":
                col += 1
            # compute rectangle size
            max_col = col
            rectangle_size = (col - col_index + 1) * (row - row_index + 1)
            max_rectangle_size = max(max_rectangle_size, rectangle_size)

        return max_rectangle_size

# test url: https://leetcode.com/problems/maximal-rectangle/


import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(
            self, 
            [[
                ["1","0","2","0","0"],
                ["2","0","4","5","6"],
                ["7","8","9","a","b"],
                ["c","0","0","d","0"]
            ]],
            self.s.maximalRectangle, 
            6
        )

    @unittest.skip
    def test_2(self):
        compare(self, [], self.s.maximalRectangle, 0)