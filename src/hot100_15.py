
# 标准答案
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()
#         ans = list()
#
#         # 枚举 a
#         for first in range(n):
#             # 需要和上一次枚举的数不相同
#             if first > 0 and nums[first] == nums[first - 1]:
#                 continue
#             # c 对应的指针初始指向数组的最右端
#             third = n - 1
#             target = -nums[first]
#             # 枚举 b
#             for second in range(first + 1, n):
#                 # 需要和上一次枚举的数不相同
#                 if second > first + 1 and nums[second] == nums[second - 1]:
#                     continue
#                 # 需要保证 b 的指针在 c 的指针的左侧
#                 while second < third and nums[second] + nums[third] > target:
#                     third -= 1
#                 # 如果指针重合，随着 b 后续的增加
#                 # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
#                 if second == third:
#                     break
#                 if nums[second] + nums[third] == target:
#                     ans.append([nums[first], nums[second], nums[third]])
#
#         return ans
#
#
# print(Solution().threeSum([-1,0,1,-1,0,1]))



class Solution:
    def threeSum(self, nums):
        res= []

        nums = sorted(nums)

        for a in range(0,len(nums)-2):


            if a>0 and nums[a] == nums[a-1]:
                continue
            i = a + 1
            j = len(nums) - 1
            while i<j:

                s = nums[a]+nums[i]+nums[j]
                if s==0:
                    res.append([nums[a],nums[i],nums[j]])
                    i+=1
                    j -= 1
                    while i<len(nums)-1 and nums[i]==nums[i-1]:
                        i+=1
                    while j>a and nums[j] == nums[j+1]:
                        j-=1


                if s<0:
                    i+=1
                if s>0:
                    j-=1
        return res


print(Solution().threeSum([-1,0,1,-1,0,1]))
