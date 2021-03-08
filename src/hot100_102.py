# 102.
# 二叉树的层序遍历
#
# 给你一个二叉树，请你返回其按
# 层序遍历
# 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3, 9, 20, null, null, 15, 7],
#
# 3
# / \
#     9
# 20
# / \
#     15
# 7
#
# 返回其层序遍历结果：
#
# [
#     [3],
#     [9, 20],
#     [15, 7]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tmp=[]
            size = len(queue)
            for i in range(size):
                s = queue.pop(0)
                tmp.append(s.val)
                if s.left:
                    queue.append(s.left)
                if s.right:
                    queue.append(s.right)
            res.append(tmp)
        return res




