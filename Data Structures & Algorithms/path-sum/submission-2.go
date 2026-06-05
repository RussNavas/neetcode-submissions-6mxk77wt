/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func hasPathSum(root *TreeNode, targetSum int) bool {
    total := 0
    return helper(root, targetSum, &total)
}

func helper(root *TreeNode, targetSum int, total *int) bool{
    if root == nil{
        return false
    }
    *total += root.Val
    if root.Left == nil && root.Right == nil && targetSum == *total{
        return true
    }
    if helper(root.Left, targetSum, total){
        return true
    }

    if helper(root.Right, targetSum, total){
        return true
    }
    *total -= root.Val
    return false
}
