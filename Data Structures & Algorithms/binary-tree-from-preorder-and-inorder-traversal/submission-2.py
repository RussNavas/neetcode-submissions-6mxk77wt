# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # base case for recursion, either list is exhausted
        if not preorder or not inorder:
            return None

        # root for a subtree (start at top of tree i.e. 1st root)
        root = TreeNode(preorder[0])

        # map the value of the root to its inorder lst
        # this will obtain a left and right subarray
        mid = inorder.index(preorder[0])
        # get the values left of the root add them to the left of the tree
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        # get the values right of the root add them to the right of the tree
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1:])
        return root