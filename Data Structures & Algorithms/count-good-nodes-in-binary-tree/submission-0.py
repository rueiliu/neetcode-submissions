'''
Apply DFS search(top-down recursive)

write a helper function that can input the current node and maxvalue
each recursion check if the node val is bigger than the max one(if yes than 1 elso 0 ) and update the maxvalue everytime
write recursion


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxval):
            if not node:
                return 0
            res = 1 if node.val >= maxval else 0
            maxval = max(maxval, node.val)
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)

            return res

        return dfs(root, root.val)

        