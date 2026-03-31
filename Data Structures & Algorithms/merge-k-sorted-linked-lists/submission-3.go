/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode{
    dummy := &ListNode{}
    dummyHead := dummy

    for l1 != nil && l2 != nil{
        if l1.Val < l2.Val{
            dummy.Next = l1
            l1 = l1.Next
        }else{
            dummy.Next = l2
            l2 = l2.Next
        }
        dummy = dummy.Next
    }

    if l1 != nil{
        dummy.Next = l1
    }
    if l2 != nil{
        dummy.Next = l2
    }
    return dummyHead.Next
}

func mergeKLists(lists []*ListNode) *ListNode {
    if len(lists) == 0{
        return nil
    }
    for i := 1; i < len(lists); i++{
        lists[i] = mergeTwoLists(lists[i-1], lists[i])
    }

    return lists[len(lists)-1]
}
