# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 1 child no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # get inorder successor i.e. left most descendent of right subtree
            minNode = self.findMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root