# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        while headA:
            s.add(id(headA))
            headA=headA.next
        while headB:
            if id(headB) in s:#here we are checking wheater id of same head is present here or not.
                return headB
            headB=headB.next
        return None
        