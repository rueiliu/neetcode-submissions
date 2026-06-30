'''
find the root that has K nodes underneath
go to the deepest left side, and store them in stacks
pop the stack and deduct k everytime
when k == 0 return current node value
after going through the left branch, go through the right branch
when 



'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []

        while curr or stack:

            # append everything into the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

        