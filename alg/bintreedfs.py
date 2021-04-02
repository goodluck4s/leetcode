# -- coding: utf-8 --


class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

_1 = Node(1)
_2 = Node(2)
_3 = Node(3)
_4 = Node(4)

_1.left = _2
_1.right = _3
_3.right = _4


def qian(root):
    stack = []

    pass

def hou(root):

    stack = []
    lis=[]

    while stack or root:
        while root:
            stack.append(root)
            lis.append(root.val)
            root = root.right

        root = stack.pop()
        root = root.left

    return lis[::-1]

print(hou(_1))