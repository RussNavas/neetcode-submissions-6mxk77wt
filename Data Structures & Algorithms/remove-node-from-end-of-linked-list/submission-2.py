# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if not head or length == 1:
            return None
        k = length - n
        if k == 0:
            return head.next
        prev = dummy
        curr = head
        while k > 0:
            prev = curr
            curr = curr.next
            k -= 1
        if prev != None:
            prev.next = curr.next if curr.next else None
        return head