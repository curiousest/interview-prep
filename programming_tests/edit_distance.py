from typing import List
from heapq import heappush, heappop

# paste solution method definition here

def estimate_distance(word1, word2):
    return max(len(set(word2) - set(word1)), len(word1) - len(word2))

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        heap = []
        estimated_distance = estimate_distance(word1, word2)
        next_distance = 0
        next_word = word1
        min_distance = max(len(word1), len(word2))
        explored = set([word1])
        while estimated_distance < min_distance:
            max_access_index = min(len(next_word) + 1, len(word2))
            max_index = min(len(next_word), len(word2))
            start_index = 0
            while start_index < max_index and next_word[start_index] == word2[start_index]:
                start_index += 1
            
            # add character
            for index in range(start_index, max_access_index):
                new_word = next_word[:index] + word2[index] + next_word[index:]
                if new_word == word2:
                    #print("Found", next_distance + 1)
                    min_distance = min(min_distance, next_distance + 1)
                elif new_word not in explored:
                    heappush(heap, (
                        estimate_distance(new_word, word2) + next_distance + 1,
                        next_distance + 1, 
                        new_word
                    ))
                    explored.add(new_word)
        
            # remove character
            for index in range(start_index, len(next_word)):
                new_word = next_word[:index] + next_word[index + 1:]
                if new_word == word2:
                    #print("Found", next_distance + 1)
                    min_distance = min(min_distance, next_distance + 1)
                elif new_word not in explored:
                    heappush(heap, (
                        estimate_distance(new_word, word2) + next_distance + 1,
                        next_distance + 1, 
                        new_word
                    ))
                    explored.add(new_word)
        
            # replace character
            for index, character in enumerate(next_word[start_index:max_access_index]):
                index = index + start_index
                if character == word2[index]:
                    continue
                new_word = next_word[:index] + word2[index] + next_word[index+1:]
                if new_word == word2:
                    #print("Found", next_distance + 1)
                    min_distance = min(min_distance, next_distance + 1)
                elif new_word not in explored:
                    heappush(heap, (
                        estimate_distance(new_word, word2) + next_distance + 1,
                        next_distance + 1, 
                        new_word
                    ))
                    explored.add(new_word)
            #print(heap)
            if heap:
                estimated_distance, next_distance, next_word = heappop(heap)
            else:
                return min_distance
        return min_distance


# test url: https://leetcode.com/problems/edit-distance/

import unittest
from utils import compare

class TestPracticeProblem(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        compare(self, ['horse', 'ros'], self.s.minDistance, 3)

    def test_2(self):
        compare(self, ['intention', 'execution'], self.s.minDistance, 5)

    def test_3(self):
        compare(self, ['a', 'ab'], self.s.minDistance, 1)