# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(val=0,next=None)
        i = l1
        j = l2
        head = pre
        while i is not None or j is not None:
            if i is None:
                pre.next=j
                break
            if j is None:
                pre.next=i
                break
            if i.val>j.val:
                pre.next = j
                j=j.next
                pre=pre.next
            else:
                pre.next = i
                i = i.next
                pre = pre.next
        return head.next
