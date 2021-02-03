# 55.
# 跳跃游戏
#
# 给定一个非负整数数组
# nums ，你最初位于数组的
# 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。
#
#
#


class Solution:
    def canJump(self, nums) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


print(Solution().canJump([2,0,0]))