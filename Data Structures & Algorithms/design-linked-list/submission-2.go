type ListNode struct {
    val int
    prev *ListNode
    next *ListNode
}

type MyLinkedList struct {
    head *ListNode
    tail *ListNode
    size int
}


func Constructor() MyLinkedList {
    head := &ListNode{val: 0}
    tail := &ListNode{val: 0}
    head.next = tail
    tail.prev = head
    return MyLinkedList {head: head, tail: tail, size: 0}
}


func (this *MyLinkedList) getPrev (index int) *ListNode {
    var cur *ListNode
    if index <= this.size / 2 {
        cur = this.head
        for i := 0; i < index; i++ {
            cur = cur.next
        }
    } else {
        cur = this.tail
        for i := 0; i < this.size-index+1; i++{
            cur = cur.prev
        }
    }
    return cur
}

func (this *MyLinkedList) Get(index int) int {
    if index >= this.size {
        return -1
    }
    return this.getPrev(index).next.val
}


func (this *MyLinkedList) AddAtHead(val int)  {
    this.AddAtIndex(0, val)
    
}


func (this *MyLinkedList) AddAtTail(val int)  {
    this.AddAtIndex(this.size, val)
}


func (this *MyLinkedList) AddAtIndex(index int, val int)  {
    if index > this.size{
        return
    }
    node := &ListNode{val: val}
    prev := this.getPrev(index)
    next := prev.next
    prev.next = node
    node.prev = prev
    node.next = next
    next.prev = node
    this.size++
}


func (this *MyLinkedList) DeleteAtIndex(index int)  {
    if index >= this.size {
        return
    }
    prev := this.getPrev(index)
    cur := prev.next
    next := cur.next
    prev.next = next
    next.prev = prev
    this.size--
}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */