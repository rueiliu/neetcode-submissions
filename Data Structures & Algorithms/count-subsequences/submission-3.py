class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        if len(t) > len(s):
            return 0

        def dfs(i, j): # i as index of s; j as index of t
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            #skip s
            res = res + dfs(i+1, j)
            if s[i] == t[j]:
                res = res + dfs(i+1, j+1)
            cache[(i, j)] = res

            return res

        return dfs(0,0)
        