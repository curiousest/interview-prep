import itertools
from fractions import Fraction

class Solution:

    def is_on_line(self, m, b, point):
        #print(point[1], m*point[0] + b)
        return point[1] == m * point[0] + b

    def maxPoints(self, points) -> int:
        if len(points) < 2:
            return len(points)
        max_points = 0
        pairs = itertools.combinations(points, 2)
        
        for pair in pairs:
            if pair[1][0] == pair[0][0]:
                max_points = max(
                    max_points,
                    sum([1 if point[0] == pair[0][0] else 0 for point in points])
                )
                continue

            m = Fraction(pair[1][1] - pair[0][1], pair[1][0] - pair[0][0])
            b = pair[0][1] - m * pair[0][0]
            pts = sum([1 if self.is_on_line(m, b, point)
                     else 0
                     for point in points])
            max_points = max(max_points, pts)
            #print(m, b, pts)
            #print('----------')
        return max_points

        # for each pair, count number of points on the line

# print(Solution().maxPoints([[1,1],[2,2],[3,3]]))
# print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
#print(Solution().maxPoints([[0,0], [0,1]]))
#print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(Solution().maxPoints([[3,1],[12,3],[3,1],[-6,-1]]))