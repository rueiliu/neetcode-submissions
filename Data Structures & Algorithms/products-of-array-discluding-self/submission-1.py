'''
1. Understand
input: a list full of nums, can be negative or zero
output: a list of the product of elements of nums except nums[i]
edge cases: element is 0 / negative element / one or two elements 

2. Plan
use the prefix and suffix list to store the left product and right product respectively




'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []
        for i in range(len(nums)):
            j = 0
            pro = 1 
            while j < i:
                pro = pro * nums[j]
                j += 1
            prefix.append(pro)

        for i in range(len(nums)):
            z = len(nums) -1
            pro = 1 
            while z > i:
                pro = pro * nums[z]
                z -= 1
            suffix.append(pro)

        return [x*y for x, y in zip(prefix, suffix)]


     
        
        