# -- coding: utf-8 --

import copy


# 预测用的维特比
def f2(mat):

    dp = copy.deepcopy(mat)

    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            dp[i][j] = max(mat[i][j]+dp[i-1][k] for k in range(len(mat[0])))

    print(dp)
    return max(dp[-1])


print(f2([[1,1,1],[1,2,3],[3,2,1]]))


