class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.max_house(nums[1:len(nums)]), self.max_house(nums[0:len(nums)-1]), nums[0])

    def max_house(self, nums):
        house1, house2 = 0, 0
        for n in nums:
            tmp = max(n+house1, house2)
            house1 = house2
            house2 = tmp

        return house2
        