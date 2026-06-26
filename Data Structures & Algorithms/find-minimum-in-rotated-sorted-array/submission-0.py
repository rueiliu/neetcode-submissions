'''
input: an array num
output: an integer(return the minimum element of this array)



Seach for minimum, binary search





'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[0]