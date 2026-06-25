'''
input: an integer array
output: return maximum water a container can store
edge case: when height is all 0/ only 2 bar
the amt should be the indices difference  times minimum height


apply two pointer technique
use left and right and mover across the bar to calculate the max amount

if a new amt is being calculated, use the max funtion to compare with the previous max amt
return the result 

'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left = 0
        right = len(heights) -1

        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            res = max(res, amount)
                
          #move the shorter height
            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1
        
        return res




            

        