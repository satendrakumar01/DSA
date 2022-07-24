# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        n=ListNode(0)
        n.next=head
        head=n
        l=r=head.next


        while(r):
            if l.val==r.val:
                r=r.next
            elif l.next==r:
                n.next=l
                n=l
                l=r
            else:
                l=r
        n.next=None if l.next else l
        return head.next
