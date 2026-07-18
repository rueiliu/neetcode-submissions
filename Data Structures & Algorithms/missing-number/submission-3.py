class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0

        for num in nums:
            if n == num:
                n += 1
            else:
                return n
        return n


        