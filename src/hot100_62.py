# 62.
# 不同路径
#
# 一个机器人位于一个
# m
# x
# n
# 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#
#
#
# 示例
# 1：
#
# 输入：m = 3, n = 7
# 输出：28


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res =[[1]*n for _ in range(m)]

        for j in range(1,m):
            for i in range(1,n):
                res[j][i]=res[j-1][i]+res[j][i-1]

        return res[-1][-1]
