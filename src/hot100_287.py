# 287.
# 寻找重复数
#
# 给定一个包含
# n + 1
# 个整数的数组
# nums ，其数字都在
# 1
# 到
# n
# 之间（包括
# 1
# 和
# n），可知至少存在一个重复的整数。
#
# 假设
# nums
# 只有
# 一个重复的整数 ，找出
# 这个重复的数 。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 3, 4, 2, 2]
# 输出：2


class Solution2:
    def findDuplicate(self, nums) -> int:

        map = {}
        for i in nums:
            if i not in map:
                map[i]=1
            else:

                return i


class Solution:
    def findDuplicate(self, nums) -> int:

        n = len(nums)
        l=1
        r = n-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            cnt = 0
