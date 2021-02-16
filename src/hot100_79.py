# 79.
# 单词搜索
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ]
#
# 给定
# word = "ABCCED", 返回
# true
# 给定
# word = "SEE", 返回
# true
# 给定
# word = "ABCB", 返回
# false


class Solution:
    def exist(self, board, word: str) -> bool:

        todo=[(0,-1),(-1,0),(0,1),(1,0)]
        stop = set([])

        r = len(board)
        c = len(board[0])

        def trace(i,j,k):
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True

            stop.add((i,j))

            # 走到这里 是部分匹配上了
            for t in todo:
                ni=i+t[0]
                nj=j+t[1]

                if 0<=ni<r and 0<=nj<c and (ni,nj) not in stop:
                    res = trace(ni,nj,k+1)
                    if res:
                        # stop.remove((i, j))  这里可以不加  就算不移除  这个return是正解 之后流程结果 移除是否无所谓了
                        return True
            stop.remove((i,j))
            return False

        for i in range(r):
            for j in range(c):
                if trace(i,j,0):
                    return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))

