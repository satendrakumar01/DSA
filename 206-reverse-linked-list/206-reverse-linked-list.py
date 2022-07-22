# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=None
        
        p,c=None,None
        while(head):
            c=head
            head=head.next
            c.next=p
            p=c
        return c
            
            
        
        