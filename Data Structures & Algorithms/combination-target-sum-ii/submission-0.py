'''
U:
input: a list of integers, target value(integer)
output: a list of list(combinations of target values)
edge cases: target value being 1 or candidates small

Match:
Backtracking problem

Plan:

create a dfs helper function, there will be index(current index), path(current combination of integers) and total(current sum)

in dfs function, write a for loop that iterate through index and to the end of the last of candidates
first check if total == target, if it does return path

to prevent duplicate path, if index < loop(i), and if integers are the same, then skip this element

then append the element into path, and call dfs function
then pop the value in path(backtracking)

outside the function call dfs


Implement
Review
Evaluate


'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        #sort first
        candidates.sort()

        def dfs(index, path, current):
            if current == target:
                res.append(path.copy())
                return 

            for i in range(index, len(candidates)):
                if index < i and candidates[i] == candidates[i-1]:
                    continue
                
                if current + candidates[i] > target:
                    return
                
                path.append(candidates[i])
                dfs(i+1, path, current+candidates[i])
                path.pop()
            
        dfs(0, [], 0)
    
        return res



        