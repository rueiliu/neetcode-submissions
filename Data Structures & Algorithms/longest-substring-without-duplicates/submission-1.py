'''
sliding window
use right to expand
when encounter a duplicate, remove left side until duplicate is gone



'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        char_set = set()

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[i])
            length = max(length, i-left + 1)


        return length
  