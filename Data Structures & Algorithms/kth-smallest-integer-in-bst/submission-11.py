# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        def inOrderTraversal(root):
            if not root:
                return root
            
            inOrderTraversal(root.left)
            inOrder.append(root)
            inOrderTraversal(root.right)

        inOrderTraversal(root)
        return inOrder[k-1].val