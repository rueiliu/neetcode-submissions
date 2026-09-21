'''

use a hashmap to store visited combinations

1. write a helper function dfs(i,j) with i,j being the index of s and p
2. first check base cases, when j >= len(p) then also check if i >= len(s)(return False if i < len(s))
3. check if s[i] == p[j], or p[j] == "."
4. two cases, when the next letter is "*", then can either forward j(zero matches) or match with s[i](thus i + 1) and store it in memo
5. if its normal match, then i+1 and j+1 and store it in memo



'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i: int, j: int) -> bool:

            if (i, j) in memo:
                return memo[(i, j)]

            if j >= len(p):
                return i >= len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j +1 ] == "*":
                #do nothing
                res = dfs(i, j + 2) or (match and dfs(i+1, j))
                memo[(i,j)] = res
                return res

            if match:
                res = dfs(i+1, j+1)
                memo[(i,j)] = res
                return res

            memo[(i, j)] = False
            return False
        return dfs(0,0)


        