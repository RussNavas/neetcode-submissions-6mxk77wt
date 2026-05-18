type ListNode struct {
    url string
    prev *ListNode
    next *ListNode
}

type BrowserHistory struct {
    cur *ListNode
}


func Constructor(homepage string) BrowserHistory {
    node := &ListNode{url: homepage}
    return BrowserHistory{cur: node}
}


func (this *BrowserHistory) Visit(url string)  {
    node := &ListNode{url: url, prev: this.cur}
    this.cur.next = node
    this.cur = this.cur.next
}


func (this *BrowserHistory) Back(steps int) string {

    for this.cur.prev != nil && steps > 0 {
        this.cur = this.cur.prev
        steps--
    }
    return this.cur.url

    
}


func (this *BrowserHistory) Forward(steps int) string {
    for this.cur.next != nil && steps > 0 {
        this.cur = this.cur.next
        steps--
    }
    return this.cur.url
}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */