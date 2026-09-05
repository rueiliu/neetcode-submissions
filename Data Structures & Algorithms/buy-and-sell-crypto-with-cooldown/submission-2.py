'''
input: a list of integer
output: an integer
maximize the profit

DP problem + dfs algorithm
calculate the best result of making a purchase/selling decision

1. first create a empty dict called dp{}, should store (day, buy or sell(boolean)) and value as maximum profit of that decision, 
2. write the dfs(day(i), boolean) function, first check the boundaries if it is still inside the boundaires, and then check if this decision has been stored
3.check buying decision, use if/else statement, if buy, use dfs to calculate result, and then compare it with doing nothing


time complexity: O(2n) -> O(n)
space complexity:O(2n) -> O(n)



'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, buy): # buy is a boolean value
            
            if i >= len(prices):
                return 0

            if (i, buy) in dp:
                return dp[(i, buy)]

            nothing = dfs(i+1, buy) # doing nothing
            # if we decided to buy
            if buy:
                buying = dfs(i+1, False) - prices[i]
                dp[(i, buy)] = max(buying, nothing)

            else: # selling
                sell = dfs(i+2, True) + prices[i]
                dp[(i, buy)] = max(sell, nothing)

            
            return dp[(i, buy)]


        return dfs(0, True)



        