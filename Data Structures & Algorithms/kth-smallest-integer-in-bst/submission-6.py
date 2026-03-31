# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        res = []
        def dfs(root, res):
            if not root:
                return None
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
            return res
        dfs(root, res)
        return res[k-1]