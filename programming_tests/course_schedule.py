from typing import List
from copy import deepcopy

# paste solution method definition here

def overlaps(item1, item2):
    return item1[0] < item2[1] and item1[1] > item2[0]

class Option:
    def __init__(self, include, exclude):
        self.include = include
        self.exclude = exclude

    def __repr__(self):
        return "Option {} | {}".format(str(self.include), str(self.exclude))

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        options = []
        max_overlap = 0
        non_empty_courses = [sorted(c) for c in courses if c[0] != c[1]] 
        for index, item in enumerate(non_empty_courses):
            to_exclude = {i + index + 1 for i, c in enumerate(non_empty_courses[index + 1:]) if overlaps(item, c)}
            #print(index, to_exclude)
            if not options:
                options = [Option(set([index]), to_exclude), Option(set(), set([index]))]
                max_overlap = 1
            else:
                for option in options:
                    if index not in option.exclude:
                        new_option = deepcopy(option)
                        new_option.exclude.add(index)
                        options.append(new_option)

                        option.include.add(index)
                        option.exclude = option.exclude | to_exclude
                        max_overlap = max(max_overlap, len(option.include))
        #print(len(courses) - len(non_empty_courses))
        #for option in options:
        #    print(option)
        return max_overlap + len(courses) - len(non_empty_courses)


# test url: https://leetcode.com/problems/course-schedule-iii/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
    @unittest.skip
    def test_1(self):
        compare(self, [[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]], self.s.scheduleCourse, 3)
    @unittest.skip
    def test_2(self):
        compare(self, [[[5,5],[4,6],[2,6]]], self.s.scheduleCourse, 2)
    
    def test_3(self):
        compare(self, [[[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]], self.s.scheduleCourse, 4)

        