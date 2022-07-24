# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        slow,fast=head,head
        while(fast and fast.next): # here we are finding weather the ll has cycle or not 
            slow=slow.next
            fast=fast.next.next
            if fast is slow:
                fast=head
                break #If cycle is found than defenitly we set fast pointer at head and traverse though out the poblem
        if fast and fast.next: #if fast may be not exitst the program will return none but if the fast.next is exist the the program will check cycle for sure and return the postion were the slow and fast pointer are equal 
            
            while slow!=fast:
                fast=fast.next
                slow=slow.next
            return fast
        return None
        