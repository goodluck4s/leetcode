# 581. 最短无序连续子数组
#
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。


# 单调栈
class Solution:
    def findUnsortedSubarray(self, nums) -> int:

        if not nums:
            return 0

        stack = [(nums[0],0)]

        lf,ri=len(nums)-1,0

        for i in range(1,len(nums)):
            if len(stack)==0 or nums[i]>=stack[-1][0]:
                stack.append((nums[i],i))
            else:
                while stack and nums[i]<stack[-1][0]:
                    top = stack.pop()
                    lf = min(lf,top[1])

        stack = [(nums[-1], len(nums)-1)]
        for i in range(len(nums)-2,-1,-1 ):
            if len(stack)==0 or nums[i] <= stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while stack and nums[i] > stack[-1][0]:
                    top = stack.pop()
                    ri = max(ri, top[1])

        print(lf,ri)
        return ri-lf+1 if ri>lf else 0
print(Solution().findUnsortedSubarray([5,4,3,2,1]))