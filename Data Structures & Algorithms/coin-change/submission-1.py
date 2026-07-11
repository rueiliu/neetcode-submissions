'''
create a list dp that stores the amount of coints that certain amt needs,
default value should be large large that can't be reached

dp[0] = 0

itirate throught amount and coins, then apply DP(bottom up)
split the question into 1+dp(amount-coins) then return dp[amount](check if it is the default value too)
set 

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

            
        return dp[amount] if dp[amount] != amount+1 else -1


        