# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # rev the second half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        # the mid point may need to be pointed toward None before reconnecting links ...
        # use the ref to the og head and the rev head and reconnect links

        head2 = prev
        while head and head2:
            h1_next = head.next
            h2_next = head2.next
            head.next = head2
            head = h1_next
            head2.next = h1_next
            head2 = h2_next