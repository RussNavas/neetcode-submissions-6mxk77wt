/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
    var isBalanced bool
    isBalanced = true
    dfs(root, &isBalanced)
    return isBalanced
}

func dfs(root *TreeNode, b *bool) int{
    if root == nil{
        return 0
    }

    leftH := dfs(root.Left, b)
    rightH := dfs(root.Right, b)
    diff := leftH - rightH
    if diff < 0{
        diff = diff * -1
    }
    if diff > 1{
        *b = false
    }
    return max(leftH, rightH) + 1
}
