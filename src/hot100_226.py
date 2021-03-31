# 226. 翻转二叉树
#
# 翻转一棵二叉树。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):

        if not root:
            return root


        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right,root.left = left,right

        return root



def f(root):
    if not root:
        return root

    left = root.f(root.left)
    right = root.f(root.right)
    root.left,root.right = right,left

    return root

