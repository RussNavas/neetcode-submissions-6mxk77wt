# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(root):
            nonlocal isBalanced

            if not root:
                return 0
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if abs(root.left - root.right) > 1:
                isBalanced = False
            return 1 + max(root.left, root.right)
        dfs(root)
        return isBalanced
            
