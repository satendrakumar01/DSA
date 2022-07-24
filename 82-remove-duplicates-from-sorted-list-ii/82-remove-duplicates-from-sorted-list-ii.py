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
            if l.val==r.val:# if l val and r val are equal move r to r.next
                
                r=r.next
            elif l.next==r: # checking distacne weather l.next if equal value of r then we conclude l to the n.next or ll and move the pointer l to r and continue the process
                n.next=l
                n=l
                l=r
            else:  # if any of the condition would not matched then we will surly move l to r 
                l=r
        n.next=None if l.next else l # after the while loop got executed then we have to check weather l.next exist or not if yes then n.next surly point to the null other wise conclued l itself in the returning head
        return head.next# just to avoid the dummy node returning the head.next
