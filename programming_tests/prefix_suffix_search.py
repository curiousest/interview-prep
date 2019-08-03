from typing import List

def add_to_hash_list(hash_, index, value):
    if index not in hash_:
        hash_[index] = set([value])
    else:
        hash_[index].add(value)

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.prefixes = {}
        self.suffixes = {}
        for index, word in enumerate(words):
            add_to_hash_list(self.prefixes, "", word)
            add_to_hash_list(self.prefixes, "", word)
            for index in range(1, len(word) + 1):
                add_to_hash_list(self.prefixes, word[:index], word)
                add_to_hash_list(self.suffixes, word[-index:], word)
        #print(self.suffixes)
        #print(self.prefixes)

    def f(self, prefix: str, suffix: str) -> int:
        if prefix == '' == suffix:
            return len(self.words) - 1
        elif prefix == '' or suffix == '':
            return -1
        matched_prefixes = self.prefixes.get(prefix, set())
        matched_suffixes = self.suffixes.get(suffix, set())
        matched_words = matched_prefixes & matched_suffixes

        #print(matched_prefixes)
        #print(matched_suffixes)
        #print(matched_words)

        for index, word in enumerate(reversed(self.words)):
            if word in matched_words:
                return len(self.words) - index - 1
        return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

def a(inp, answer_func, sol):
    print('-------------')
    result = answer_func(*inp)
    if result != sol:
        print('Input: ', inp)
        print('Real answer: ', sol)
        print('Answer: ', result)
    else:
        print('Correct ', result)

s = WordFilter(["apple"])
a(["a", "e"],s.f, 0)
a(["b", ""],s.f, -1)
a(["", ""], s.f, 0)

s = WordFilter(["pop"])
a(["p",""], s.f, -1)

["WordFilter","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f","f"]
[[["pop"]],["",""],["","p"],["","op"],["","pop"],["p",""],["p","p"],["p","op"],["p","pop"],["po",""],["po","p"],["po","op"],["po","pop"],["pop",""],["pop","p"],["pop","op"],["pop","pop"],["",""],["","p"],["","gp"],["","pgp"],["p",""],["p","p"],["p","gp"],["p","pgp"],["pg",""],["pg","p"],["pg","gp"],["pg","pgp"],["pgp",""],["pgp","p"],["pgp","gp"],["pgp","pgp"]]