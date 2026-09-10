'''

1. break the problem into sub problems
2. slice the array by first searching for the last one to burst

top down method / dp method

1. gonna add 1 to the top and end of the array for virtual boudaries
2. write a dfs helper function that will perfom dp, also create a dict: cache to store the results of repeated calculations. and also store the result in res
3. first check if nums still has integers in it and if it has been calculated. 
4. perform dp by dividing the problem into subproblems and calculate current value, then compare with res and update if current value is greater than res
5. return and call the dfs function


'''


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]
        cache = {}
        

        def dfs(l, r):
            
            if l + 1 >= r:
                return 0

            if (l, r) in cache:
                return cache[(l, r)]
            # iterate through nums
            res = 0
            for k in range(l+1, r):
                current_val = dfs(l, k) + dfs(k, r) + A[l] * A[r] * A[k]
                res = max(res, current_val)

            cache[(l, r)] = res
            return res

        return dfs(0, len(A) - 1)



            
        