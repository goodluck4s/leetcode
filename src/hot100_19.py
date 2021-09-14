class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if not head:
            return None
        res = ListNode(-1,head)

        a = head
        b= res
        k=0
        while k<n-1:
            a=a.next
            k+=1
        while a.next:
            a=a.next
            b=b.next
        b.next = b.next.next
        return res.next


head = ListNode(3,None)
head = ListNode(2,head)
head = ListNode(1,head)
i=head
while i != None:
    print(i.val)
    i=i.next

Solution().removeNthFromEnd(head,1)

