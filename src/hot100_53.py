# 53. 最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


# 回溯  解释对的  但是运行超时 2^n
class Solution2:
    def maxSubArray(self, num) -> int:
        if len(num)<=1:
            return sum(num)
        res = sum(num)
        return max(res, self.maxSubArray(num[1:]), self.maxSubArray(num[:-1]))


# 保存中间结果  分治
class Solution:
    def maxSubArray(self, num) -> int:
        if len(num)<=1:
            return sum(num)
        res = [0] * len(num)
        res[0] = sum(num)
        for i in range(len(num)):



print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
