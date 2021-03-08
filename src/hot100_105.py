# 105. 从前序与中序遍历序列构造二叉树
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# O(n)
class Solution1:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]


            root = TreeNode(preorder[preorder_root])

            size_left_subtree = inorder_root - inorder_left

            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                    inorder_root - 1)
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                     inorder_right)
            return root

        n = len(preorder)

        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


# O()
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def myBuildTree(a,b):
            if not a:
                return None
            if not b:
                return None

            j = b.index(a[0])
            root = TreeNode(a[0])

            b_left = j-0

            root.left = myBuildTree(a[1:1+b_left],b[:j])
            root.right = myBuildTree(a[1+b_left:],b[j+1:])
            return root


        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(preorder,inorder)


Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])



