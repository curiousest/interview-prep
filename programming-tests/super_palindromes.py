import math
from itertools import combinations

def is_palindrome2(num):
    str_item = str(num)
    middle = len(str_item) // 2
    if len(str_item) % 2 == 1:
        middle += 1

    print(str_item[:middle])
    print(str_item[-middle:])
    return str_item[:middle] == str_item[-middle:]

def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]
    

class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L_sqrt = math.ceil(math.sqrt(int(L)))
        R_sqrt = math.floor(math.sqrt(int(R)))

        palindromes_in_range = []
        for len_num in range(len(str(R_sqrt))):
            middle = len(str_item) // 2
            if len(str_item) % 2 == 1:
                middle += 1

            for half_palindrome in permutations([[range(1,)]]):


        super_palindromes = 0

        for item in range(L_sqrt, R_sqrt + 1):
            # item is palindrome
            if is_palindrome(item) and is_palindrome(item ** 2):
                super_palindromes += 1
        return super_palindromes

s = Solution()

def a(L, R, answer_func, sol):
    print('-------------')
    result = answer_func(L, R)
    if result != sol:
        print('Input: ', L, R)
        print('Real answer: ', sol)
        print('Answer: ', result)
    else:
        print('Correct ', result)

a("4", "1000", s.superpalindromesInRange, 4)

