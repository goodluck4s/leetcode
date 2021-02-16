# 78.
# 子集
#
# 给你一个整数数组
# nums ，数组中的元素
# 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集
# 不能
# 包含重复的子集。你可以按
# 任意顺序
# 返回解集。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3]
# 输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
#
# 示例
# 2：
#
# 输入：nums = [0]
# 输出：[[], [0]]


class Solution2:
    def subsets(self, nums):
        t=[]
        ans=[]

        def dfs(cur, nums):
            if cur ==len(nums):
                ans.append(t[:])
                return
            t.append(nums[cur])
            dfs(cur+1,nums)
            t.pop()
            dfs(cur + 1, nums)


        dfs(0, nums)
        return ans



class Solution:
    def subsets(self, nums):
        res=[]
        tmp=[]
        ans=[]
        def f(n):
            if len(tmp)==n:
                res.append(tmp[:])
                e=[]
                for i in range(n):
                    if tmp[i]==1:
                        e.append(nums[i])
                ans.append(e)
                return
            for i in [0,1]:
                tmp.append(i)
                f(n)
                tmp.pop()
        f(len(nums))
        print(ans)

        return ans


print(Solution().subsets([1,2,3,4]))
# import numpy as np
# a=np.array([1,2,3])
# b=np.array([0,0,1])
# print(a[[1,2]])

