# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # consider that for each subtree we have a bound for the left and right child
        # that is  -inf < left child < root and root < right child < inf for a valid subtree
        # user recursion to update the relavent bounds

        def isValid(node, left_bound, right_bound):
            if not node:
                return True
            if not (left_bound < node.val < right_bound):
                return False
            
            return (
                isValid(node.left, left_bound, node.val) and
                isValid(node.right, node.val, right_bound)
            )
        return isValid(root, float("-inf"), float("inf"))