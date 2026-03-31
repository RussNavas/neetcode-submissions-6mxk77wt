# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        prev = None
        cur = s.next
        s.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        l1 = head
        l2 = prev

        while l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2


        
        