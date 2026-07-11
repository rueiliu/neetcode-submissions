'''
Create a hashmap, with keys being the index, value being the ways of combination
when index being len(s)(crossed the finishing line) that means this is one combination

use dynamic programming(for loop) starting from the last index and move forward

use two cases(when slice one, firts chekc if it's zero, if zero dp[i]=0]), this means one combinaion found

then check for slice 2(remember only 26 alphabets) then add the previous calculation to the slice 2 dp[i+2] result

return the result





'''



class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if (i+1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] = dp[i] + dp[i+2]

        return dp[0]





        