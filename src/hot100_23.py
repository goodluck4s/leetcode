# 23. 合并K个升序链表

# 可以依赖合并两个有序链表这样  顺序合并 复杂度O(k*k*n)

# 分治合并O(log(k)*k*n)  递推可以推出
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(val=0, next=None)
        i = l1
        j = l2
        head = pre
        while i is not None or j is not None:
            if i is None:
                pre.next = j
                break
            if j is None:
                pre.next = i
                break
            if i.val > j.val:
                pre.next = j
                j = j.next
                pre = pre.next
            else:
                pre.next = i
                i = i.next
                pre = pre.next
        return head.next



    def mergeKLists(self, lists) -> ListNode:
        if lists is None or len(lists)==0:
            return None
        n = len(lists)
        if n==1:
            return lists[0]
        else:
            mid=n//2
            a = self.mergeKLists(lists[:mid])
            b = self.mergeKLists(lists[mid:])
            return self.mergeTwoLists(a,b)


