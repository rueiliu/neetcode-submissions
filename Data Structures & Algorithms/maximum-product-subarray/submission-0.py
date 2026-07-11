'''
create res for maximum result(set default as maximum value, like singel)
create curMax, curMin(min for if its super negative and next one is negative then it will become super postivie)

if num == 0, reset the calculation

use for loop to update curMax, curmin
then compare with res

return res



'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for num in nums:
            tmp = curMax
            curMax = max(num, num*curMax, num*curMin)
            curMin = min(num, tmp*num, num*curMin)
            res = max(res, curMax)
        return res