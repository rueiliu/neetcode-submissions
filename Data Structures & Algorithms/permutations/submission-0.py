'''
backtracking problem

U: 
input: list of integers output: list of list(combinations)

M: backtracking

P:

should have res(store result)
path(current combination)
and a set -> used to record used

use a helper function, first check base case(if len(path) == len(nums), if it does then append copy of path into res

then use for loop to iterate through all elements, first check if element has been used, if not then path and used append, then call the helper function again then pop elements out of path and used

at the end call the helper function

'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # store the result
        path = [] # store combinations
        used = set()

        def backtrack():
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue
                else:
                    path.append(num)
                    used.add(num)

                    backtrack()

                    path.pop()
                    used.remove(num)

            
        backtrack()
        return res

        