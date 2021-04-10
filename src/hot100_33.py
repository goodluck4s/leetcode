# 33.
# 搜索旋转排序数组
#
# 升序排列的整数数组
# nums
# 在预先未知的某个点上进行了旋转（例如， [0, 1, 2, 4, 5, 6, 7]
# 经旋转后可能变为[4, 5, 6, 7, 0, 1, 2] ）。
#
# 请你在数组中搜索
# target ，如果数组中存在这个目标值，则返回它的索引，否则返回 - 1 。
#
#
#
# 示例
# 1：
#
# 输入：nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# 输出：4
#
# 示例
# 2：
#
# 输入：nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# 输出：-1
#
# 示例
# 3：
#
# 输入：nums = [1], target = 0
# 输出：-1


# 拓展内容 折半查找
def bs(nums,tar):
    i,j = 0,len(nums)-1

    while i<=j:
        mid = (i+j)//2
        if nums[mid]==tar:
            return mid
        if nums[0] < nums[mid]:
            # 左边有序
            if nums[i] <=tar<= nums[mid]:
                j=mid-1
            else:
                i=mid+1
        else:
            #右边有序
            if nums[mid] <=tar<= nums[j]:
                i=mid+1
            else:
                j=mid-1


print(bs([3,4,5,1,2],4))


class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[i]:
                # 左边有序
                if nums[i]<=target<nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            else:
                # 右边有序
                if nums[mid]<target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1

