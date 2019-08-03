from typing import List
import itertools
import queue

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        tree_order = sorted([i for i in itertools.chain(*forest) if i > 1])
        print(tree_order)
        if not tree_order:
            return 0
        if forest[0][0] == tree_order[0]:
            del tree_order[0]
        if not tree_order:
            return 0

        overall_steps = 0
        start_row = 0
        start_col = 0

        for target_tree in tree_order:
            q = queue.Queue()
            q.put((start_row, start_col, 0))
            visited = set([(start_row, start_col)])
            minimum_steps = None
            while not q.empty():
                #print(stack)
                try_row, try_col, curr_steps = q.get()
                for delta_row in [-1, 0, 1]:
                    for delta_col in [-1, 0, 1]:
                        if abs(delta_col) == abs(delta_row): continue
                        new_row = try_row + delta_row
                        new_col = try_col + delta_col

                        in_bounds = new_row >= 0 and new_col >= 0 and \
                            new_row < len(forest) and new_col < len(forest[0]) and \
                            forest[new_row][new_col] != 0

                        if in_bounds:
                            if forest[new_row][new_col] == target_tree:
                                # found the tree
                                if minimum_steps is None or curr_steps + 1 < minimum_steps:
                                    minimum_steps = curr_steps + 1
                                    start_row = new_row
                                    start_col = new_col

                                minimum_steps = min(curr_steps + 1, minimum_steps) if minimum_steps is not None else curr_steps + 1
    
                            if (new_row, new_col) not in visited:
                                q.put((new_row, new_col, curr_steps + 1))
                                visited.add((new_row, new_col))
            print(target_tree, minimum_steps)

            if minimum_steps is None:
                return -1
            else:
                overall_steps += minimum_steps
        return overall_steps
            
import unittest
from utils import compare

class TestGolf(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    @unittest.skip
    def test_basic(self):
        compare(self, [[
            [1,2,3],
            [0,0,4],
            [7,6,5]
            ]], self.s.cutOffTree, 6
        )

    def test_2(self):
        compare(self, [[
            [1,2,3],
            [0,0,0],
            [7,6,5]
            ]], self.s.cutOffTree, -1
        )

    def test_3(self):
        compare(self, [[
            [2,3,4],
            [0,0,5],
            [8,7,6]
            ]], self.s.cutOffTree, 6
        )
 
    @unittest.skip
    def test_larger(self):
        compare(self, [[
            [9, 12,5, 14],
            [17,11,13,15],
            [2, 20,19,21],
            [16,4, 7, 8],
            [18,3, 6, 10]]], self.s.cutOffTree, 57
        )