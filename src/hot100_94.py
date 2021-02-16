# 94. 二叉树的中序遍历
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


_8 = TreeNode(8)
_9 = TreeNode(9)
_6 = TreeNode(6,_8,_9)
_7 = TreeNode(7)
_4 = TreeNode(4)
_5 = TreeNode(5)

_2 = TreeNode(2,_4,_5)
_3 = TreeNode(3,_6,_7)
_1 = TreeNode(1,_2,_3)

def qian(root):
    if root:
        print(root.val)
        qian(root.left)
        qian(root.right)

def zhong(root):
    if root:
        zhong(root.left)
        print(root.val)
        zhong(root.right)

def hou(root):
    if root:
        hou(root.left)
        hou(root.right)
        print(root.val)

zhong(_1)


class Solution:
    def inorderTraversal(self, root: TreeNode):



