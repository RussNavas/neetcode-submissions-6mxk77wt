# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #base case
        if not head or not head.next:
            return head

        # recurse
        new_head = self.reverseList(head.next)

        #work
        nxt = head.next
        nxt.next = head
        head.next = None

        #return
        return new_head
        