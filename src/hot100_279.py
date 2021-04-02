# 279. 完全平方数
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

import math
#
class Solution:
    def numSquares(self, n: int) -> int:

        ma = math.floor(math.sqrt(n))+1
        ch = [x*x for x in range(1,ma)]
        print("ch",ch)

        dp = [0]*(n+1)

        for i in range(1,n+1):

            tmp_lis = [dp[i-x]+1 if i-x>=0 else 9999 for x in ch]
            print(tmp_lis)
            dp[i] = min(tmp_lis)
        print(dp)
        return dp[-1]

Solution().numSquares(9)


