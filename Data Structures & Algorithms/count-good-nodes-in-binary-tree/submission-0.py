# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxNum):

            if not node:
                return 0
            
            count = 0

            if node.val >= maxNum:
                count = 1
            
            maxNum = max(node.val, maxNum)

            return (count + dfs(node.left, maxNum) + dfs(node.right, maxNum))
        
        return (dfs(root, root.val))

            

        

            
