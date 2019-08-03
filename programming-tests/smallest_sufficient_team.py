from typing import List
from itertools import combinations, chain

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_set = set(req_skills)

        for team_size in range(1, len(people) + 1):
            for team in combinations(list(enumerate(people)), team_size):
                if skill_set == set(chain(*[member[1] for member in team])):
                    return [member[0] for member in team]

s = Solution()

print(s.smallestSufficientTeam(["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]))
#Output: [0,2]


print(s.smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]))
#Output: [1,2]