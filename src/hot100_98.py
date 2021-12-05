# 98. 验证二叉搜索树
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#     节点的左子树只包含小于当前节点的数。
#     节点的右子树只包含大于当前节点的数。
#     所有左子树和右子树自身必须也是二叉搜索树。
#
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import sys


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        stack = []
        trace = -1 * sys.maxsize

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val < trace:
                return False
            trace = root.val
            root = root.right

        return True


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        def f(index, lower, upper):
            if not index:
                return True
            v = index.val
            t = lower < v and v < upper
            return t and f(index.left, lower, v) and f(index.right, v, upper)

        return f(root, float("-inf"), float("inf"))
