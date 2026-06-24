'''
Understand
1. input: an array of integers nums
2. output: the length of the longest consectuvie sequence
3. Non-sequential
4. edge cases: zero/few elements 


Plan
1. can use Hash set to avoid iterating through the list
2. create a variable called length and store the maximum length in it
2. check if each element of nums is in set_nums, if it is then check 










'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if (num + 1) not in set_nums:
                length = 1
                while (num - length) in set_nums:
                    length += 1
                longest = max(length, longest)
                 
        return longest

        