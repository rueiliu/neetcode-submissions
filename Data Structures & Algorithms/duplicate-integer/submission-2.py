class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set()
        for num in nums:
            if num in new_nums:
                return True
            new_nums.add(num)
        
        return False
        