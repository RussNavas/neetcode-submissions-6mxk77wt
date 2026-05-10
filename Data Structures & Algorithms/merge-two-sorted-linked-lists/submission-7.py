# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l1, l2 = list1, list2
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1 or l2:
            dummy.next = l1 if l1 else l2
        return head.next
