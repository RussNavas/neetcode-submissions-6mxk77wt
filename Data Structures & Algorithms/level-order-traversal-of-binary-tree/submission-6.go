/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
    res := [][]int{}

    if root == nil{
        return res
    }

    q := []*TreeNode{root}

    for len(q) > 0{
        floor := []int{}
        qLen := len(q)
        for i := 0; i < qLen; i++{
            curr := q[0]
            q = q[1:]
            floor = append(floor, curr.Val)
            if curr.Left != nil{
                q = append(q, curr.Left)
            }
            if curr.Right != nil {
                q = append(q, curr.Right)
            }
            
        }
        res = append(res, floor)
        floor = []int{}

    }
    return res
}
