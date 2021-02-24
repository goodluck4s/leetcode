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

qian(_1)


class Solution:
    def zhongxu(self, root: TreeNode):
        res = []
        stack = []
        index = root
        while index or stack:
            while index:
                stack.append(index)
                index = index.left

            index = stack.pop()
            res.append(index.val)
            index = index.right

        return res


    def qianxu(self,root):
        res=[]
        stack=[]
        index = root

        while index or stack:
            while index:
                res.append(index.val)
                stack.append(index)
                index=index.left

            index = stack.pop()
            index = index.right
        return res


    def shendu(self,root):
        if not root:
            return
        res=[]
        stack=[]
        stack.append(root)

        while stack:
            index = stack.pop()
            res.append(index.val)
            if index.right:
                stack.append(index.right)
            if index.left:
                stack.append(index.left)
        return res

    def guangdu(self,root):
        if not root:
            return
        res=[]
        stack=[]
        stack.append(root)

        while stack:
            index = stack.pop(0)
            res.append(index.val)
            if index.left:
                stack.append(index.left)
            if index.right:
                stack.append(index.right)

        return res





print(Solution().guangdu(_1))









