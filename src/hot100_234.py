# 234. 回文链表
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True
        mid = self.find_mid(head)
        if mid==head:
            if head.next==None:
                return True
            else:
                return head.val==head.next.val

        sec = mid.next
        mid.next=None

        sec = self.revese(sec)

        i,j=head,sec
        while i and j:
            if i.val!=j.val:
                return False
            i=i.next
            j=j.next

        return True



    def find_mid(self,head):
        f,s = head,head

        while f.next and f.next.next:
            s=s.next
            f=f.next.next

        return s

    def revese(self,head):

        pre,cur = None,head

        while cur:
            tmp=cur.next
            cur.next=pre
            pre = cur
            cur=tmp
        return pre



