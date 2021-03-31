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

        def f(root,k,res):
            if not root:
                return
            sum += root.val
            if sum-root.val in dic:
                res+=dic[sum-root.val]

            dic[sum]=dic.get(sum,0)+1

            f(root.left,sum,res)
            f(root.right,sum,res)
        res=0
        f(root,sum,res)
        return res
