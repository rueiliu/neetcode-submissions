'''
greedy solution
start from the last index, check if the number closest to the last index can reach last indext
if can, update the target to the closest number(using for loop)

at last check if the closest number is at index 0


'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= pos:
                pos = i


        return True if pos == 0 else False
        

        