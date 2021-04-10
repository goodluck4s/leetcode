# 39. 组合总和
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#     所有数字（包括 target）都是正整数。
#     解集不能包含重复的组合。
#
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
#
# 示例 2：
#
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

from typing import List

# 标准答案
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


# 用不剪枝的回溯  会有bug就是 不同顺序的集合也会重复出现在res里
class Solution:
    def combinationSum(self, candidates, target: int):

        if not candidates:
            return []

        # candidates = sorted(candidates, reverse=False)

        res = []
        tmp=[]
        def func(b):
            gap = target-sum(tmp)
            if gap>0:
                for i in range(b,len(candidates)):
                    tmp.append(candidates[i])
                    func(i)
                if tmp:
                    tmp.pop()
            if gap<0:
                tmp.pop()
                return
            if gap==0:
                res.append(tmp[:])
                tmp.pop()
                return

        func(0)

        return res



print(Solution().combinationSum([2,3,6,7],7))

# this_case_demo

#                []
#             /      \
#           [1]       [2]
#         /    \        \
#      [1,1]    [1,2]      [2,2]
#     /     \
# [1,1,1]  [1,1,2]


class Solution:
    def combinationSum(self, candidates, target: int):

        if not candidates:
            return []

        # candidates = sorted(candidates, reverse=False)

        res = []
        tmp=[]
        def func(b):
            if sum(tmp)>=target:
                if sum(tmp)==target:
                    res.append(tmp[:])

                return
            for i in range(b,len(candidates)):
                tmp.append(candidates[i])
                func(i)
                tmp.pop()

        func(0)
        print(res)

        return res


Solution().combinationSum([2,3,6,7],7)


def func(s):
    res=[]
    tmp=[]

    def f(i):
        if len(tmp)==i:
            res.append("".join(tmp))
            return
        for j in range(i,len(s)):
            tmp.append(s[j])
            f(j+1)
            tmp.pop()
    f(0)
    print(res)
func("aab")


