# https://leetcode.com/problems/dungeon-game/

class Solution:
    def possible_moves(self, x, y, dungeon):
        possibilities = []
        if x < len(dungeon) - 1: 
            possibilities.append((x + 1, y))
        if y < len(dungeon[0]) - 1:
            possibilities.append((x, y+1))
        return possibilities
    
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if len(dungeon) == 1 and len(dungeon[0]) == 1:
            return max(-dungeon[0][0] + 1, 1)
        queue = [[dungeon[0][0], dungeon[0][0], (0, 0)], ]
        paths = []
        while queue:
            path = queue.pop(0)
            x, y = path[-1]
            for next in self.possible_moves(x, y, dungeon):
                path[0] = path[0] + dungeon[next[0]][next[1]]
                path[1] = min(path[0], path[1])
                print(path[0])
                print(path[1])
                print(path + [next])
                if next[0] == len(dungeon) - 1 and next[1] == len(dungeon[0]) - 1:
                    paths.append(path + [next])
                else:
                    queue.append(path + [next])
        for path in paths:
            print(path)
        return max(-sorted(map(lambda a: a[1], paths))[-1] + 1, 1)

