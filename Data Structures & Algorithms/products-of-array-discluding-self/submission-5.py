'''
1. Understand
input: a list full of nums, can be negative or zero
output: a list of the product of elements of nums except nums[i]
edge cases: element is 0 / negative element / one or two elements 

2. Plan
use the prefix and suffix list method
first we will create a res list, with a length of nums
then iterate through the nums, while first time changing the res into the product of left elements
then iterate agaian, this time change the res into the product of right elements




'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        product = 1
        for i in range(len(nums)):
            res[i] = product 
            product = nums[i] * product

        product2 = 1

        for i in range(len(nums)-1, -1 , -1):
            res[i] = product2 * res[i]
            product2 = nums[i] * product2

        return res








