# 72.
# 编辑距离
#


# 回溯
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        tmp = 0 if word1[0] == word2[0] else 1
        return min(self.minDistance(word1[1:], word2) + 1, self.minDistance(word1, word2[1:]) + 1,
                   self.minDistance(word1[1:], word2[1:]) + tmp)

# 动归
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        mat = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word1)):
            mat[0][i+1] = i+1
        for j in range(len(word2)):
            mat[j+1][0] = j+1

        for i in range(len(word1)):
            for j in range(len(word2)):
                tmp = 0 if word1[i] == word2[j] else 1
                mat[j+1][i+1] = min(mat[j][i+1]+1,mat[j+1][i]+1,mat[j][i]+tmp)
        return mat[-1][-1]

print(Solution().minDistance("horse","ros"))