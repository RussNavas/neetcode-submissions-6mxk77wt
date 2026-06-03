/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rightSideView(root *TreeNode) []int {
    res := []int{}
    if root == nil{
        return res
    }

    q := []*TreeNode{root}

    for len(q) > 0{
        rightside := []int{}
        rightside = append(rightside, q[len(q)-1].Val)
        res = append(res, rightside...)
        qLen := len(q)
        for i := 0; i < qLen; i++{
            curr := q[0]
            q = q[1:]
            if curr.Left != nil{
                q = append(q, curr.Left)
            }
            if curr.Right != nil {
                q = append(q, curr.Right)
            }
        }
    }
    return res
}
