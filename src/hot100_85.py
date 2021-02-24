# 85. 最大矩形
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。



class Solution2:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        tmp=[[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if j==0:
                    tmp[i][j]=int(matrix[i][j])
                else:
                    tmp[i][j] = 0 if int(matrix[i][j])==0 else tmp[i][j-1]+1
        print(tmp)

        ret = 0
        for i in range(row):
            for j in range(col):
                if int(matrix[i][j])==0:
                    continue
                width = tmp[i][j]
                area = width
                for k in range(i-1,-1,-1):
                    width = min(width,tmp[k][j])
                    area = max(area, (i - k + 1) * width)
                ret = max(area,ret)
        return ret


# 转化成84题
class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        tmp=[[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if j==0:
                    tmp[i][j]=int(matrix[i][j])
                else:
                    tmp[i][j] = 0 if int(matrix[i][j])==0 else tmp[i][j-1]+1
        print(tmp)



        def largestRectangleArea(heights) -> int:
            if not heights:
                return 0

            l = []
            r = [0] * len(heights)
            stack = []

            for i in range(len(heights)):
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                l.append(stack[-1] if stack else -1)
                stack.append(i)

            stack = []
            for j in range(len(heights) - 1, -1, -1):
                while stack and heights[j] <= heights[stack[-1]]:
                    stack.pop()
                r[j] = stack[-1] if stack else len(heights)
                stack.append(j)

            return max([heights[i] * (r[i] - l[i] - 1) for i in range(len(heights))])

        ret = 0
        for j in range(col):
            height = [tmp[i][j] for i in range(row)]
            tmp_res = largestRectangleArea(height)
            print(tmp_res,height)
            if tmp_res>ret:
                ret = tmp_res
        return ret



print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
