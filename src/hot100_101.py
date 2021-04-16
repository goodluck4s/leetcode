# 101.
# 对称二叉树
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树[1, 2, 2, 3, 4, 4, 3]
# 是对称的。
#



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack1=[root]
        stack2=[root]

        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1.val!=top2.val:
                return False

            l1 = top1.left is not None
            r1 = top1.right is not None
            l2 = top2.left is not None
            r2 = top2.right is not None

            if not( (l1 and r2) or (l1==False and r2==False)):
                return False
            if not( (r1 and l2) or (r1==False and l2==False)):
                return False
            if top1.left and top2.right:
                stack1.append(top1.left)
                stack2.append(top2.right)
            if top1.right and top2.left:
                stack1.append(top1.right)
                stack2.append(top2.left)


        return len(stack1)==0 and len(stack2)==0





class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:

        def f(n1,n2):
            if n1 and n2:
                return n1.val==n2.val and f(n1.left,n2.right) and f(n1.right,n2.left)
            else:
                if n1 ==None and n2==None:
                    return True
                else:
                    return False

        return f(root,root)


