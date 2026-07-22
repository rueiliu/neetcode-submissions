'''
use stack 

iterate(for loop) through each bar and store them inside my stack (index, height)

when we encounter a bar that is shorter than the latest elements in stack's height


calculat the curren area using a max function(continue to pop left until we found a bar shorter)


at last, use another for loop to calculate the maximum area(if there's no heights lower in front to block the bar)




'''

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))


        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)-i) )
        
        return maxArea

