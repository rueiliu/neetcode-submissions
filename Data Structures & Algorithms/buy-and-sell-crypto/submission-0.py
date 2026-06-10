class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # set a var called max_profit to record the current maxium profit
        # set a var called low_price to record the current lowest price
        # iterate through every day's price as the selling price and 
        # see if the max_profit is larger than what the previous ones


        max_profit = 0
        low_price = prices[0]

        for pr in prices:
            low_price = min(pr, low_price)
            max_profit = max(max_profit, pr-low_price)
        return max_profit
            

        