/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    if node == nil {
        return node
    }

    oldToNew := make(map[*Node]*Node)


    var helper func(node *Node) *Node
    helper = func(node *Node) *Node{

        if _, ok := oldToNew[node]; ok {
            return oldToNew[node]
        }
        clone := &Node{Val: node.Val}
        oldToNew[node] = clone

        for _, n := range node.Neighbors{
            clone.Neighbors = append(clone.Neighbors, helper(n))
        }

        return clone
    }
    return helper(node)
}
