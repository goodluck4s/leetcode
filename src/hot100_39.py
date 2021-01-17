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


class Solution:
    def combinationSum(self, candidates, target: int):

        nums = sorted(candidates, reverse=True)

        res = []
        tmp = []

        def func(nums, tar, i):
            if not nums:
                return

            if i >= len(nums):
                tmp.clear()
                func(nums[1:], tar, 0)
                return
            else:
                if nums[i]>target:
                    func(nums[1:], tar, 0)
                    return
                if nums[i]==target:
                    res.append([nums[i]])
                    func(nums[1:], tar, 0)
                    return
                tmp.append(nums[i])

            now = sum(tmp)

            if now == tar:
                res.append(tmp[:])
                tmp.pop()
                func(nums, tar, i + 1)

            if now < tar:
                func(nums, tar, i)

            if now > tar:
                tmp.pop()
                func(nums, tar, i + 1)

        func(nums, target, 0)

        return res


print(Solution().combinationSum([2,3,6,7], 7))
