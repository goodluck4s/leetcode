# 2. 两数相加
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        i,j = l1,l2
        jinwei = 0
        res=ListNode(-1,None)
        k = res
        while i !=None or j!=None:
            a = jinwei
            if i!=None:
                a+=i.val
            if j!=None:
                a+=j.val

            k.next = ListNode(int(str(a)[-1]), None)
            if a>=10:

                jinwei=1
            else:
                jinwei=0

            k=k.next
            if i != None:
                i=i.next
            if j != None:
                j=j.next
        if jinwei ==1:
            k.next = ListNode(1, None)


        return res.next

