# 53. 最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


# 回溯  解释对的  但是运行超时 2^n
class Solution2:

    def maxSubArray(self, num) -> int:
        if len(num)<=1:
            return sum(num)
        res = sum(num)
        return max(res, self.maxSubArray(num[1:]), self.maxSubArray(num[:-1]))

print(Solution2().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



# 动归
class Solution3:
    def maxSubArray(self, num) -> int:
        if len(num)<=1:
            return sum(num)
        res = num[0]
        pre = 0

        for i in range(len(num)):
            pre = max(pre+num[i],num[i])
            res = max(res,pre)
        return res


# 动归 分解分析
class Solution_inspect:
    def maxSubArray(self, num) -> int:
        if len(num)<=1:
            return sum(num)

        tmp = []
        tmp.append(num[0])

        arr_arr = []
        arr_arr.append([num[0]])

        for i in range(1, len(num)):
            if tmp[i-1]+num[i]>num[i]:
                tmp.append(tmp[i-1]+num[i])
                tl = arr_arr[i-1][:]
                tl.append(num[i])
                arr_arr.append(tl)
            else:
                tmp.append(num[i])
                arr_arr.append([num[i]])

        print(tmp)
        print(arr_arr)

        return max(tmp)


# 分治
class Solution:
    def maxSubArray(self, num) -> int:
        if len(num)<=1:
            return sum(num)

        def f(nums):
            if len(nums)==1:
                l = nums[0]
                r = nums[0]
                m = nums[0]
                n = nums[0]
                return l,r,m,n

            mid = len(nums)//2
            a_l,a_r,a_m,a_n = f(nums[:mid])
            b_l,b_r,b_m,b_n = f(nums[mid:])
            n = a_n+b_n  # 留n是为了求l r
            l= max(a_l,a_n+b_l)  # 留 lr 是为了求m
            r = max(b_r,b_n+a_r)  # 留 lr 是为了求m
            m = max(a_m,b_m,a_r+b_l)
            return l,r,m,n

        return f(num)[-2]



print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
