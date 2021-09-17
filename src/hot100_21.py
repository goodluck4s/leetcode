# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1,None)
        p=res
        a=l1
        b=l2
        while a and b:
            if a.val>=b.val:
                p.next = b
                b=b.next
                p=p.next
            else:
                p.next=a
                a=a.next
                p=p.next
        if a is not None:
            p=a
        if b is not None:
            p=b
        return res.next


