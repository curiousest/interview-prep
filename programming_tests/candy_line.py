class Solution:
    def candy(self, ratings) -> int:
        candies = [1 for _ in ratings]
        for i in range(len(ratings)):
            if i != 0:
                if ratings[i-1] < ratings[i] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i -1] + 1 
            if i != len(ratings) - 1:
                if ratings[i+1] < ratings[i] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i+1] + 1
        print(candies)
        for i in reversed(range(len(ratings))):
            if i != 0:
                if ratings[i-1] < ratings[i] and candies[i] <= candies[i - 1]:
                    candies[i] = candies[i -1] + 1 
            if i != len(ratings) - 1:
                if ratings[i+1] < ratings[i] and candies[i] <= candies[i + 1]:
                    candies[i] = candies[i+1] + 1
        print(candies)
        return sum(candies)
s = Solution()

#print(s.candy([1,0,2]))
#print(s.candy([1,2,2]))
print(s.candy([1,2,87,87,87,2,1]))