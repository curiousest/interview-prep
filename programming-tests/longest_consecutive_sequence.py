from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(list(set(nums)))
        #print(nums_sorted)

        last = None
        consecutive = 0
        longest_consecutive = 0
        for item in nums_sorted:
            if last is None or item - last == 1:
                consecutive += 1
                longest_consecutive = max(longest_consecutive, consecutive)
            else:
                consecutive = 1
            last = item
        return longest_consecutive
s = Solution()


def a(inp, answer, sol):
    print('-------------')
    if answer != sol:
        print('Input: ', inp)
        print('Real answer: ', answer)
        print('Answer: ', sol)
    else:
        print('Correct ', sol)

a([100, 4, 200, 1, 3, 2], 4, s.longestConsecutive([100, 4, 200, 1, 3, 2]))
a([1,2,0,1], 3, s.longestConsecutive([1,2,0,1]))
a([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645], 3, s.longestConsecutive([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]))
