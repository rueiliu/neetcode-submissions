'''
use dfs/recursion to solve

create a empty list called res

then write the recursion function, passing (i, curr, total)
with i being the index, curr being the curr combination we have found, and total being the current sum
in the recursion function first check if the total meets the target, if it meets appned curr to res

also make sure i < len(nums) and total < target
update total while adding one more to i everytime
use recursion to calculate the two different cases exceed or still under target


'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            curr.pop()
            dfs(i+1, curr, total)
            

           

        dfs(0, [], 0)
        return res


            
        