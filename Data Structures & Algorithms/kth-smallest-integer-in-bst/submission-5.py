# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = k
        def _dfs(root):
            nonlocal count, res
            if not root:
                return
            _dfs(root.left)
            count -= 1
            if count == 0:
                res = root.val
                return
            _dfs(root.right)
        _dfs(root)
        return res