class Solution:
    def moveZeroes(self, nums) -> None:
        i,j=0,0

        while j<len(nums):
            if nums[j]==0:
                j+=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
        print(nums)
        return nums

Solution().moveZeroes([0,1,0,3,12])