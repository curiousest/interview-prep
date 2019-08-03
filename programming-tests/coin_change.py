from typing import List
import copy

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        
        explored = set()
        explored.add(amount)
        curr_amount = -1
        sorted_coins = list(sorted(coins))
        
        while curr_amount != amount:
            print("RETRY")
            num_coins = 0
            curr_amount = amount
            to_explore = copy.copy(sorted_coins)

            while to_explore:
                coin = to_explore.pop()
                try_amount = curr_amount - coin
                if try_amount in explored or try_amount < 0:
                    print("not", coin)
                    continue
                elif try_amount == 0:
                    num_coins += 1
                    return num_coins
                elif try_amount not in explored:
                    print(coin)
                    num_coins += 1
                    curr_amount = try_amount
                    explored.add(try_amount)
                    to_explore = copy.copy(sorted_coins)
        return -1

s = Solution()
def a(inp, answer_func, sol):
    print('-------------')
    result = answer_func(*inp)
    if result != sol:
        print('Input: ', inp)
        print('Real answer: ', sol)
        print('Answer: ', result)
    else:
        print('Correct ', result)

#a([[1, 2, 5], 11], s.coinChange, 3)
#a([[4, 11], 12], s.coinChange, 3)
a([[186,419,83,408], 6249], s.coinChange, 20)