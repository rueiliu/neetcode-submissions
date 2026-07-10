'''
set a pair of index for the start and end of the string
create an array of Boolean valule to store whether specific strings are palindrome.

use two for loop to check if there's palindrome, update the array(Boolean value)
and update the index


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i+1):
                        resIdx = i
                        resLen = (j-i+1)

        
        return s[resIdx: resIdx+resLen]
        