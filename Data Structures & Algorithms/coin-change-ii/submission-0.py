
#top-down approach
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        cache = {}

        def dfs(i, a): # i is the index number of coin while a is the amount of coin, we're trying to fill up the table
            #base case
            if a == amount:
                return 1

            if a > amount:
                return 0

            if (i,a) in cache:
                return cache[(i, a)]

            if i >= len(coins):
                return 0

            cache[(i,a)] = dfs(i+1, a) + dfs(i, a + coins[i])


            return cache[(i,a)]

        return dfs(0, 0)        