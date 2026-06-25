'''
1. Understand
input: integer array nums
output: triplets of sum = 0 in a list, non sequential
indices are distinct
edge cases: many duplicate values

2. Plan

two pointer technique
left right, and scan thorugh the middle elements everytime
use unumertae so can track the index
no duplicates





'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        #set a fixed position and apply the two pointer technique
        #use unumertae so can track the index

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                constant = a + nums[left] + nums[right]
                
                if constant > 0:
                    right -= 1
                elif constant < 0:
                    left += 1
                else:
                    res.append([a, nums[right], nums[left]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
        return res
     

          




        