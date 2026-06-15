/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    oldToNew := map[*Node]*Node{}

    var dfs func(*Node) *Node
    dfs = func(node *Node) *Node{
        if val, ok := oldToNew[node]; ok{
            return val
        }
        clone := &Node{Val: node.Val}
        oldToNew[node] = clone

        for _, n := range node.Neighbors{
            clone.Neighbors = append(clone.Neighbors, dfs(n))
        }
        return clone
    }
    if node == nil{
        return nil
    }
    return dfs(node)
}
