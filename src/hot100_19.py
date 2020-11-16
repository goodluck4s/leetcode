class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


head = ListNode(3,None)
head = ListNode(2,head)
head = ListNode(1,head)
i=head
while i != None:
    print(i.val)
    i=i.next

Solution().removeNthFromEnd(head,1)

