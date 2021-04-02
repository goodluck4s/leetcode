# 437. 路径总和 III
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        dic = {0:1}
        res=0

        def f(root,k):
            nonlocal res
            if not root:
                return
            k += root.val
            if k-sum in dic:
                res+=dic[k-sum]

            dic[k-sum]=dic.get(k-sum,0)+1

            f(root.left,k)
            f(root.right,k)
            dic[k - sum] = dic.get(k - sum, 0) -1

        f(root,0)
        return res
