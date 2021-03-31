# 560. 和为K的子数组
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。




class Solution:
    def subarraySum(self, nums, k: int) -> int:

        count = 0
        pre = 0
        mp ={0:1}  # 这个map每个key 表示一个和的情况  value的每个数 表示从0到目前为止的一个字数组  sum(values)=len(nums)

        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in mp:
                count += mp.get(pre - k)

            mp[pre] = mp.get(pre, 0) + 1

        print(sum(list(mp.values())))

        print(count)
        return count




Solution().subarraySum([1,-1,1,1,1,2,1,2,3],4)

