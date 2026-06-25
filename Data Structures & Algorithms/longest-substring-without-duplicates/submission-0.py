'''
sliding window
use right to expand
when encounter a duplicate, remove left side until duplicate is gone



'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        left = 0
        cnt = 0

        for right in range(len(s)):
            
            while s[right] in res:
                res.remove(s[left])
                left = left+1
            
            res.add(s[right])
            cnt = max(cnt, right-left +1)

        return cnt