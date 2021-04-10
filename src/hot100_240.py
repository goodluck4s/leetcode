
# 240. 搜索二维矩阵 II
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
#     每行的元素从左到右升序排列。
#     每列的元素从上到下升序排列。


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        def f(nums,k):
            i,j=0,len(nums)-1

            while i<=j:
                mid=(i+j)//2
                if nums[mid]==k:
                    return mid
                else:
                    if k<nums[mid]:
                        j=mid-1
                    else:
                        i=mid+1
            return -1
        for nums in matrix:
            res = f(nums,target)
            if res!=-1:
                return True
            return False