'''
create a list dp consists of Boolean value that stores whether this index can lead to a word in dictionary

use dynamic programming(check from back), write a for loop to check

next index = True, so the former index can also be true
therefore, we can only check if dp[0] is true to know if s can be segmented

'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True


        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break

        return dp[0]

        