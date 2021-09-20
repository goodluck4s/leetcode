# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 答案1  传统办法
# class Solution:
#     def mergeKLists(self, lists):
#         if not lists:
#             return None
#         a = lists[0]
#         for b in lists[1:]:
#             a=self.func(a,b)
#         return a
#
#
#     def func(self,l1,l2):
#         res = ListNode(-1,None)
#         a=l1
#         b=l2
#         p=res
#         while a and b:
#             if a.val>=b.val:
#                 p.next = b
#                 b=b.next
#                 p=p.next
#             else:
#                 p.next=a
#                 a=a.next
#                 p=p.next
#         if a:
#             p.next =a
#         if b:
#             p.next=b
#         return res.next

#  1n + 2n + 3n +  ...  + kn = k*k*n = O(k*k*n)


#  答案2 分治法
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        res = self.merge(lists)
        return res[0]

    def merge(self,lists):

        if len(lists)<=1:
            return lists
        else:
            mid = len(lists)//2
            a = self.merge(lists[:mid])
            b = self.merge(lists[mid:])
            return self.func(a,b)


    def func(self,l1,l2):
        res = ListNode(-1,None)
        a=l1[0]
        b=l2[0]
        p=res
        while a and b:
            if a.val>=b.val:
                p.next = b
                b=b.next
                p=p.next
            else:
                p.next=a
                a=a.next
                p=p.next
        if a:
            p.next =a
        if b:
            p.next=b
        return [res.next]

test_case = [[1,4,5],[1,3,4],[2,6]]
test_lists=[]
for i in test_case:
    res = ListNode(-1,None)
    p=res
    for j in i:
        p.next = ListNode(j,None)
        p=p.next
    test_lists.append(res.next)
print(len(test_lists))


Solution().mergeKLists(test_lists)