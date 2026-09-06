'''
apply a top-down approach
1. write a dfs helper function for dp, helper function should be (i, amt) i as index of nums, amt is current amt. in helper function will store each nums' position into cache(dict)
2. initiate dfs(0, 0)



'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}

        def dfs(i, amt):
            # base case

            if (i, amt) in cache:
                return cache[(i, amt)]

            if i >= len(nums):
                return 1 if amt == target else 0

            cache[(i, amt)] = dfs(i+1, amt + nums[i]) + dfs(i+1, amt - nums[i])

            return cache[(i, amt)]
        return dfs(0, 0) 
        