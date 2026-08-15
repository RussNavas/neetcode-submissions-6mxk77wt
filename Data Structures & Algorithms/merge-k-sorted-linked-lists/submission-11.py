# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.merge2Lists(l1, l2))
            lists = merged
        return lists[0]

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        d = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            else:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
        dummy.next = l1 or l2
        return d.next