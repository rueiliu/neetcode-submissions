class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = nums.copy()
        new_nums.sort()
        for i in range(0, len(new_nums)-1):
            if new_nums[i] == new_nums[i+1]:
                return True
        
        return False
        