# 56. 合并区间
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].



class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals
        res=[]
        intervals = list(sorted(intervals,key=lambda x:x[0]))

        b=intervals[0][0]
        e = intervals[0][1]

        for i in intervals:
            if b<=i[0]<=e:
                e = max(e,i[1])
            else:
                res.append([b,e])
                b=i[0]
                e=i[1]
        res.append([b, e])
        return res


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

