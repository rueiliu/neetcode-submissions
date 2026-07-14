'''

create two variables maxnum and cursum. 
maxsum: maximum number recorded; cursum: curretn subarray sum

use for loop to add numbers and update the cursum.
when cursum is below 0, set cursum to 0 bc the subarray should be reset here(negative always worse)
time compleixty would be O(n), and space compleixty should be O(1)



'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for num in nums:
            if cursum < 0:
                cursum = 0

            cursum += num

            maxsum = max(maxsum, cursum)


        return maxsum

        