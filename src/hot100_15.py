class Solution:
    def threeSum(self, nums):

        n = len(nums)
        if n<3:
            return []
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n-2):
            # 需要和上一次枚举的数不相同
            if nums[first] > 0:
                continue
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            second = first+1
            third = n - 1
            while third>second:
                tmp = nums[first]+nums[second]+nums[third]
                if tmp>0:
                    third -= 1
                    while nums[third]==nums[third+1] and third>second:
                        third-=1
                if tmp<0:
                    second += 1
                    while nums[second] == nums[second-1] and third>second:
                        second += 1
                if tmp==0:
                    ans.append([nums[first], nums[second], nums[third]])
                    third -= 1
                    while nums[third]==nums[third+1] and third>second:
                        third-=1
                    second += 1
                    while nums[second] == nums[second-1] and third>second:
                        second += 1



        return ans

print(Solution().threeSum([-1,0,1,-1,0,1]))
