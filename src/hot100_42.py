# 42.
# 接雨水
#
# 给定
# n
# 个非负整数表示每个宽度为
# 1
# 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例
# 1：
#
# 输入：height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 输出：6
# 解释：上面是由数组[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 表示的高度图，在这种情况下，可以接
# 6
# 个单位的雨水（蓝色部分表示雨水）。
#
# 示例
# 2：
#
# 输入：height = [4, 2, 0, 3, 2, 5]
# 输出：9

# 两边循环 中心扩展  n^2复杂度
class Solution4:
    def trap(self, height) -> int:
        if not height or len(height) <= 2:
            return 0
        res = 0

        for i in range(0, len(height) - 1):
            l, r = 0, 0
            for j in range(0, i + 1):
                l = max(l, height[j])
            for j in range(i, len(height)):
                r = max(r, height[j])
            res += min(l, r) - height[i]
        return res


# 双指针
class Solution2:
    def trap(self, height) -> int:
        if not height or len(height) <= 2:
            return 0
        res = 0

        i, j = 0, len(height) - 1
        l, r = height[0], height[-1]

        while j >= i:
            if height[j] > height[i]:
                if height[i] > l:
                    l = height[i]
                res += l - height[i]
                i += 1
            else:
                if height[j] > r:
                    r = height[j]
                res += r - height[j]
                j -= 1
        return res


# 栈
class Solution:
    def trap(self, height) -> int:
        if not height or len(height) <= 2:
            return 0
        res = 0

        current = 0
        stack = []
        while current < len(height):
            while len(stack) > 0 and height[current] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                res += distance * bounded_height

            stack.append(current)
            current += 1

        return res


print(Solution().trap([3,2,1,0,2,3]))


def func(height):

    i,j=0,len(height)-1
    l,r=height[0],height[-1]
    res=0

    while i<=j:
        if height[i]<height[j]:
            l=max(height[i],l)
            res+=l-height[i]
            i+=1
        else:
            r = max(r,height[j])
            res+=r-height[j]
            j-=1
    return res
