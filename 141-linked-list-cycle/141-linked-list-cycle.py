# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return 0
        if head and not head.next:
            return 0
        slow,fast=head,head
        while fast and fast.next :
            slow=slow.next
            fast=fast.next.next
            if slow ==fast:
                return 1
        return 0
        