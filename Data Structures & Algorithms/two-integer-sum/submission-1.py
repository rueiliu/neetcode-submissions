class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lst = {}
        length = len(nums)
        for i in range(length):
            remain = target - nums[i]
            if remain in lst:
                return [lst[remain], i]
            if nums[i] not in lst:
                lst[nums[i]] = i
                
          
        

        