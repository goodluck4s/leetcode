

class Solution:
    def maxProduct(self, nums) -> int:

        dpma = [None]*len(nums)
        dpmi = [None]*len(nums)

        dpma[0] = nums[0]
        dpmi[0] = nums[0]
        for i in range(1,len(nums)):


            dpma[i] = max(dpma[i-1]*nums[i],dpmi[i-1]*nums[i],nums[i])
            dpmi[i] = min(dpma[i-1]*nums[i],dpmi[i-1]*nums[i],nums[i])



        return max(dpma)