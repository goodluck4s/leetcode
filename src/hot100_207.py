# 207. 课程表
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
#     例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。


# 深度优先

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:

        mapping = {}
        for i in prerequisites:
            lis = mapping.get(i[0],[])
            lis.append(i[1])
            mapping[i[0]] = lis
        vis = [0]*numCourses

        def f(v):
            vis[v]=1
            res = True
            for i in mapping.get(v,[]):
                if vis[i]==1:
                    return False
                elif vis[i]==0:
                    vis[i]=1
                    res = res and f(i)
            vis[v]=2
            return res

        res =True
        for v in range(numCourses):
            if vis[v]==0:
                res = res and f(v)
        return res


Solution().canFinish(3,[[0,1],[0,2],[1,0]])


