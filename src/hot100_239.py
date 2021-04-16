# 239.
# 滑动窗口最大值
#
# 给你一个整数数组
# nums，有一个大小为
# k
# 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的
# k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#

import heapq

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans

Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)



