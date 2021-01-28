# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

class Solution:
    def rotate(self, matrix) -> None:
        if not matrix:
            return
        n = len(matrix)

        for i in range(n // 2):
            for j in range(n - 2 * i - 1):
                #                 tmp = d
                #                 d=c   matrix[n-i-j-1][i]
                #                 c=b   matrix[n-i-1][n-i-j-1]
                #                 b=a   matrix[j+i][n-i-1]
                #                 a=tmp   matrix[i][j+i]
                tmp = matrix[n - i - j - 1][i]
                matrix[n - i - j - 1][i] = matrix[n - i - 1][n - i - j - 1]
                matrix[n - i - 1][n - i - j - 1] = matrix[j + i][n - i - 1]
                matrix[j + i][n - i - 1] = matrix[i][j + i]
                matrix[i][j + i] = tmp
        return matrix