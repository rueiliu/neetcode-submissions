'''
either use two pointer or DP to solve

first create result and n = len(s)

then dp(default False)

then use the for loop to check if it is a palindrome
if it is mark dp as true and plus result by 1


'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j-i) <= 2 or dp[i+1][j-1]):
                    res += 1
                    dp[i][j] = True


        return res
        