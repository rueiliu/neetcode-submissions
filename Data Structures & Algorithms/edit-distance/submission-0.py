'''

dp problem
translate insert/delete/replace into (i+-1)(j+-1)

1. create a dp grid, and fill the dp grid from bottom up (the last col and row) which means word1/word2 are zero while the other one is not
2. write double for loop, calculate the min of val of the grid based on the three decisions
3. return the top-left of the grid





'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # fill the bottom row
        for i in range(len(word2) + 1):
            dp[len(word1)][i] = len(word2) - i

        for j in range(len(word1) + 1):
            dp[j][len(word2)] = len(word1) - j

        
        for i in range(len(word1) -1 , -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                # perform operation
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]

        