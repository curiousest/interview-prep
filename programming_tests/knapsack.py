from typing import List

# paste solution method definition here
class Solution:
    def recursive_knapsack(self, values: List[int], weights: List[int], knapsack_size: int) -> int:
        if knapsack_size <= 0 or len(weights) == 0:
            return 0

        next_item_value = values[0]
        next_size = knapsack_size - weights[0]

        excluded_value = self.recursive_knapsack(values[1:], weights[1:], knapsack_size)
        if next_size >= 0:
            included_value = self.recursive_knapsack(values[1:], weights[1:], next_size)
        else:
            return excluded_value
        return max(included_value + next_item_value, excluded_value)
    
    def dp_knapsack(self, values: List[int], weights: List[int], knapsack_size: int) -> int:
        k = [[0 for _ in range(knapsack_size + 1)] for value in values]
        for i, value in enumerate(values):
            weight = weights[i]
            for j in range(knapsack_size + 1):
                if value < 0 or weight > j:
                    k[i][j] = k[max(0, i-1)][j]
                else:
                    k[i][j] = max(
                        k[i-1][j],
                        k[i-1][j-weight] + value
                    )
        return k[-1][-1]

        
# test url: 

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [[ 20, 5, 10, 40, 15, 25 ], [ 1, 2, 3, 8, 7, 4 ], 10], self.s.recursive_knapsack, 60)

    def test_2(self):
        compare(self, [[ 20, 5, 10, 40, 15, 25 ], [ 1, 2, 3, 8, 7, 4 ], 10], self.s.dp_knapsack, 60)


