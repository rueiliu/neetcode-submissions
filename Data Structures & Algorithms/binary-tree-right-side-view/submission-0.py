'''
Apply BFS Search

create a variable called rightvalue to store the rightmost value
use a for loop to iterate through the deque and if there's value in deque store it in rightmost variable
then append node.left and node.right to deque



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque([root])

        while q:
            rightmost = None

            for i in range(len(q)):
                node = q.popleft() # FIFO
                
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                result.append(rightmost.val)

        return result




        