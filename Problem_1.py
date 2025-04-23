
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        result = []
        if root == None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            temp = None
            size = len(queue)
            for i in range(0,size):
                node = queue.popleft()
                temp=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(temp)
        return result
            

        