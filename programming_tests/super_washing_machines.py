from typing import List
from heapq import heappop, heappush
import itertools

# paste solution method definition here
class Solution:
    def choose_possibilities(self, machines: List[int], index: int, machine: int):
        possibilities = [(machine, 'no_op')]
        change_left = index != 0 and machines[index - 1] <= machine
        change_right = index != len(machines) - 1 and machines[index + 1] <= machine
        if change_left:
            possibilities.append((machine, 'l'))
        if change_right:
            possibilities.append((machine, 'r'))
        if change_left and change_right:
            possibilities.append((machine, 'b'))
        return possibilities

    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines) !=0:
            return -1

        explored = set(str(machines))
        to_explore = [(0, machines)]
        min_found = 99999999
        while to_explore:
            turns, machines = heappop(to_explore)
            if turns > min_found:
                return turns
            possibilities = []
            for index, machine in enumerate(machines):
                possibilities.append(self.choose_possibilities(machines, index, machine))
            possible_operations_lists = itertools.product(*possibilities)
            for possible_operations_list in possible_operations_lists:
                for index, (item, operation) in enumerate(possible_operations_list):
                    if operation == 'l':
                        possible_operations_list[index - 1] = (possible_operations_list[index - 1][0]+1, possible_operations_list[index - 1][1])
                        possible_operations_list[index][0] -=1
                    elif operation == 'r':
                        possible_operations_list[index + 1][0] += 1
                        possible_operations_list[index][0] -=1
                    elif operation == 'b':
                        possible_operations_list[index + 1][0] += 1
                        possible_operations_list[index - 1][0] += 1
                        possible_operations_list[index][0] -=2
                    possible_machines = [i[0] for i in possible_operations_list]
                    if len(set(possible_machines)) == 1:
                        min_found = min(turns + 1, min_found)
                        continue
                    if str(possible_machines) not in explored:
                        heappush(to_explore, (turns + 1, possible_machines))


# test url: https://leetcode.com/problems/super-washing-machines/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, [[1,0,5]], self.s.findMinMoves, 3)

    def test_2(self):
        compare(self, [ [0,3,0]], self.s.findMinMoves, 2)

    def test_3(self):
        compare(self, [[0,2,0]], self.s.findMinMoves, -1)