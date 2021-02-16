# 84. 柱状图中最大的矩形
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


# 回溯 剪枝
import functools
class Solution2:
    def largestRectangleArea(self, heights) -> int:
        if not heights:
            return 0

        @functools.lru_cache()
        def f(i,j):
            if j-i==1:
                return heights[i:j][0]
            c = min(heights[i:j])
            k = j-i
            squa = c*k
            return max(squa,f(i+1,j),f(i,j-1))
        return f(0,len(heights))


print(Solution2().largestRectangleArea([2,1,5,6,2,3]))




# 两次循环
class Solution3:

    def largestRectangleArea(self, heights) -> int:

        if not heights:
            return 0

        m=0

        for i in range(len(heights)):
            k = heights[i]
            for j in range(i,len(heights)):
                if heights[j]<k:
                    k=heights[j]
                chang = j-i+1
                kuan = k
                s = chang*kuan
                if s>m:
                    m=s

        return m


# 两次循环2  以height[i]为中心 中心扩展
class Solution4:

    def largestRectangleArea(self, heights) -> int:

        if not heights:
            return 0
        m=0
        # 以height[i]为高
        for i in range(len(heights)):
            l=i
            while l>0 and heights[l]>=heights[i]:
                l-=1
            r = i
            while r<len(heights)-1 and heights[r]>=heights[i]:
                r+=1

            squa = heights[i]*(r-l-1)
            m = max(squa,m)

        return m
print(Solution4().largestRectangleArea([2,1,5,6,2,3]))


# 单调栈
class Solution:
    def largestRectangleArea(self, heights) -> int:
        if not heights:
            return 0

        l = []
        r=[0]*len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            l.append(stack[-1] if stack else -1)
            stack.append(i)

        stack = []
        for j in range(len(heights)-1,-1,-1):
            while stack and heights[j]<=heights[stack[-1]]:
                stack.pop()
            r[j] = stack[-1] if stack else len(heights)
            stack.append(j)

        return max([heights[i]*(r[i]-l[i]-1) for i in range(len(heights))])


print(Solution().largestRectangleArea([2,1,5,6,2,3]))