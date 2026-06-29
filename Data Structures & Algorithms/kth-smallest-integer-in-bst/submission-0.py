# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # DFS Traversal
        
        self.count = 0
        self.answer = 0

        def dfs(root):

            if not root:
                return

            dfs(root.left) # left

            self.count += 1 # self
            if self.count == k:
                self.answer = root.val

            dfs(root.right) # right

        dfs(root)
        return self.answer
            

    