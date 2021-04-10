# 494. 目标和
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。



class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        if not nums:
            return 0

        dp = [[0]*(3000) for _ in range(len(nums))]

        for i in range(S-1000,S+1000):
            t = 0
            if nums[0] == i:
                t += 1
            if -1 * nums[0] == i:
                t += 1
            dp[0][i] = t

        # print(dp)

        for i in range(1,len(nums)):
            for j in range(S-1000,S+1000):

                a =dp[i-1][j-nums[i]]
                b =dp[i-1][j+nums[i]]
                dp[i][j] = a+b

        # print(dp)
        return dp[len(nums)-1][S]


print(Solution().findTargetSumWays([0,1],1))
