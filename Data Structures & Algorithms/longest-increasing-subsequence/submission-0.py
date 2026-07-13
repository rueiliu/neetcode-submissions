'''
create a list and store every index with 1

create double for loops(stating from the last) 
if former is smaller than latter, add the latter value to the former


retunr max(list)




'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LST = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    LST[i] = max(1+LST[j], LST[i])


        return max(LST)
        