# 297. 二叉树的序列化与反序列化
#
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def func1(self,root,res):
        if root:
            res.append(root.val)
            res = self.func1(root.left,res)
            res = self.func1(root.right,res)
            return res
        else:
            res.append(None)
            return res

    def serialize(self, root):
        res = self.func1(root,[])
        return res

    def func2(self,res):
        if res:
            val = res.pop(0)
            if val:
                node = TreeNode(val)
                node.left=self.func2(res)
                node.right=self.func2(res)
                return node
            else:
                return None
        else:
            return None

    def deserialize(self, data):
        return self.func2(data)


a = Codec().deserialize([1,2,None,None,3,4,None,None,5,None,None])
print(a)
print(Codec().serialize(a))
