# 31.
# 下一个排列
#
# 实现获取
# 下一个排列
# 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须
# 原地
# 修改，只允许使用额外常数空间。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 2, 3]
# 输出：[1, 3, 2]

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead. 1243
        """
        if not nums:
            return nums

        i=len(nums)-2

        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=len(nums)-1
            while j>=0 and nums[j] <=nums[i]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]

        l,r = i+1,len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            r-=1
            l+=1
        return nums








