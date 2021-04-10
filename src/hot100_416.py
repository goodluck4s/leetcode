#
# 416. 分割等和子集
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
#     每个数组中的元素不会超过 100
#     数组的大小不会超过 200
#
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].




class Solution:
    def canPartition(self, nums) -> bool:

        if len(nums)<=1:
            return False

        s = sum(nums)
        if s%2==1:
            return False

        s = s//2
        print(s)

        dp = [[False]*(s+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True


        for i in range(1,len(nums)):
            for j in range(s+1):
                if j>=nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[-1][s]



print(Solution().canPartition([28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79]))