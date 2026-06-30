'''
BFS algorith

if root is None, return True
create a deque that store root, infinituly small val, ifinitely big val
then create while loop(condition when deque has sth in it) when check if left < value < right
then append if left/right leaf exist, if exist, append the node into the deque





'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q = deque()
        q.append((root, float("-inf"), float("inf")))

        if not root:
            return True

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False

            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right,node.val,right))
        
        return True