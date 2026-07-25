'''
Floyd's Cycle Detection Algorithm

slow/fast pointer

when they intersect, put slow back to start, and create a new slow2 at the intersection
then at the intersecton of slow and slow2 is the answer

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow
        