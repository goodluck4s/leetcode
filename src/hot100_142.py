# 142. 环形链表 II
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
#
# 说明：不允许修改给定的链表。
#
# 进阶：
#
#     你是否可以使用 O(1) 空间解决此题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set([])
        pre = head
        while pre:
            if pre not in s:
                s.add(pre)
                pre = pre.next
            else:
                return pre
        return None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = head
        fast = head

        while fast:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                return None

            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr
        return None


a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = b

Solution().detectCycle(a)
