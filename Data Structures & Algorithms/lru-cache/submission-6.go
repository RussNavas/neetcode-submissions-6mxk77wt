type Node struct {
    Key     int
    Value   int
    Prev    *Node
    Next    *Node
}

type LRUCache struct {
    Head        *Node
    Tail        *Node
    Cache       map[int]*Node
    Capacity    int
}

func Constructor(capacity int) LRUCache {
    head := &Node{}
    tail := &Node{}
    head.Next = tail
    tail.Prev = head
    cache := make(map[int]*Node)
    return LRUCache{
        Head: head,
        Tail: tail,
        Cache: cache,
        Capacity: capacity,
    }
    
}

func (this *LRUCache) Get(key int) int {
    if node, ok := this.Cache[key]; ok{
        this.RemoveNode(node)
        this.AddNode(node)
        return node.Value
    }
    return -1
}

func (this *LRUCache) Put(key int, value int) {
    if node, ok:= this.Cache[key]; ok{
        node.Value = value
        this.RemoveNode(node)
        this.AddNode(node)
    }else{
        newNode := &Node{Key:key, Value:value}
        this.Cache[key] = newNode
        this.AddNode(newNode)
    }
    if len(this.Cache) > this.Capacity{
        evictNode := this.Tail.Prev
        delete(this.Cache, evictNode.Key)
        this.RemoveNode(evictNode)
    }
}

func (this *LRUCache) AddNode(node *Node){
    // Always adds node to front of LRUCache
    oldFront := this.Head.Next
    node.Next = oldFront
    this.Head.Next = node
    oldFront.Prev = node
    node.Prev = this.Head
}

func (this *LRUCache) RemoveNode(node *Node){
    before := node.Prev
    after := node.Next
    before.Next = after
    after.Prev = before

}
