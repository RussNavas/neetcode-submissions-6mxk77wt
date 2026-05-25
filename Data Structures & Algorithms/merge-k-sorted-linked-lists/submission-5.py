# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists[0] == []:
            return 
        for i in range(1, len(lists)):
           lists[0] = self._helper(lists[0], lists[i])
        return lists[0]

    def _helper(self, l1, l2):
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return head.next