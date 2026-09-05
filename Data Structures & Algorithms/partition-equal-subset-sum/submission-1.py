'''
time complexity: O(target * n)

space complexity: O(target)



'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        total = sum(nums)
        
        # if total can't be divided equally, then its false
        if total % 2:
            return False

        target = total // 2

        for num in nums:
            copy = dp.copy()
            for current_sum in dp:
                new_sum = current_sum + num
                if new_sum == target:
                    return True
                if new_sum < target:
                    copy.add(new_sum)

            dp = copy

        return target in dp




        