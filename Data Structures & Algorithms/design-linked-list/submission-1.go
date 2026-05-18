type ListNode struct {
    val int
    next *ListNode
}

type MyLinkedList struct {
    head *ListNode
    size int
}


func Constructor() MyLinkedList {
    return MyLinkedList{
        head: &ListNode{val: 0},
        size: 0}
}


func (this *MyLinkedList) getPrev (index int) *ListNode {
    cur := this.head
    for i := 0; i < index; i++ {
        cur = cur.next
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
    prev := this.getPrev(index)
    node := &ListNode{val: val, next: prev.next}
    prev.next = node
    this.size++
}


func (this *MyLinkedList) DeleteAtIndex(index int)  {
    if index >= this.size{
        return
    }
    prev := this.getPrev(index)
    prev.next = prev.next.next
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