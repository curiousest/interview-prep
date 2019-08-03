import itertools

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        reduced_p = list(itertools.chain(*[list(g) if k != '*' else ['*'] 
                         for k, g in itertools.groupby(p)]))
        print(reduced_p)
        return self.recurse_match(s, reduced_p)

    def recurse_match(self, s: str, p: str) -> bool:
        #print(s, p, sep='   ')
        if len(s) == 0:
            return all(map(lambda a: a == '*', p))
        elif len(p) == 0:
            return False
        
        if p[0] == '*':
            # pattern match where * is empty character
            result = self.recurse_match(s, p[1:])
            if result:
                return True
            
            # pattern match the rest
            index_of_pattern, next_pattern = next( ((i, x) for (i, x) in enumerate(p) if x != '*'), (None, None))
            if next_pattern is None:
                return True
            if next_pattern == s[0]:
                result = self.recurse_match(s[1:], p[index_of_pattern:])
                if result:
                    return True
            return self.recurse_match(s[1:], p)
        elif p[0] == '?' or p[0] == s[0]:
            return self.recurse_match(s[1:], p[1:])
        else:
            # s[0] != p[0]
            return False

s = Solution()

#print(s.isMatch('aa', 'a'))
#print(s.isMatch('aa', '*'))
#print(s.isMatch('cb', '?a'))
#print(s.isMatch('adceb', 'a*b'))
#print(s.isMatch('acdcb', 'a*c?b'))
#print(s.isMatch('acdcb', '*a*b'))
print(s.isMatch("bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab","b*b*ab**ba*b**b***bba"))