'''
think of a 2 dimension graph, with i(text1) amd j(text2) of index of letters for the two words, default should be zero
goal is to find the value of top right index value, and each could be calculated from adding up from its diagonal neighbor

dynamic programming
when index values equal, add from diagonal, else pick max value from either bottom or right


'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp =[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] #found a new letter, so plus 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
        