'''

recursive
create a function to check two trees are the same
run the recursive function through root vs subroot OR leaf vs subroot

 edge case: two tress identical and 
 when doing tree problems, always check whether the root id None



'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #when subtree is None, it is a subtree of any tree
            return True
        if not root:
            return False

        if self.sametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def sametree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode])-> bool:
            
            # when both
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sametree(root.left, subRoot.left) and self.sametree(root.right, subRoot.right)
        return False