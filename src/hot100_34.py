# 34. 在排序数组中查找元素的第一个和最后一个位置
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
#     你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


class Solution:
    def searchRange(self, nums, target):

        def func(nums,tar,to_right):
            i,j = 0,len(nums)-1
            while i<=j:
                mid = (i+j)//2
                if nums[mid]==tar:
                    if to_right:
                        if mid+1<=len(nums)-1 and nums[mid+1]==tar:
                            i=mid+1

                        else:
                            return mid
                    else:
                        if mid-1>=0 and nums[mid-1]==tar:
                            j=mid-1
                        else:
                            return mid
                else:
                    if tar<nums[mid]:
                        j=mid-1
                    else:
                        i=mid+1


            return -1


        l,r = func(nums,target,False),func(nums,target,True)
        print(l,r)
        return l,r

Solution().searchRange([2,2],2)