'''
BFS search algorithm
first create a res list and a deque, then append the root into the deque
then use a while loop (when the deque has value inside)
and then a for loop to iterate through the value inside the deque, while also creating a empty list to store the result
each itereation will popleft the node from the deque(this is the node)
then if node is not None, then append its value into a list then move the root to left/right
and append the list to res
return res

edge cases: one level


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        q = deque()
        q.append(root)

        while q:
            level = []
            resLen = len(q)
            for i in range(resLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res