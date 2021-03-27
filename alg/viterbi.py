# -- coding: utf-8 --

import copy

# 算分母用的动归
def f(mat):

    dp = copy.deepcopy(mat)

    for i in range(1,len(mat)):
        for j in range(len(mat[0])):

            dp[i][j] = sum(mat[i][j]+dp[i-1][k] for k in range(len(mat[0])))

    print(dp)
    return sum(dp[-1])


print(f([[1,1,1],[1,1,1]]))

# 预测用的维特比
def f2(mat):

    dp = copy.deepcopy(mat)

    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            dp[i][j] = max(mat[i][j]+dp[i-1][k] for k in range(len(mat[0])))

    print(dp)
    return max(dp[-1])


print(f2([[1,1,1],[1,2,3],[3,2,1]]))


import math
# 算分母用的动归 全集合
def f3(mat,trans_mat):

    dp = copy.deepcopy(mat)

    for i in range(1,len(mat)):
        for j in range(len(mat[0])):

            dp[i][j] = sum(math.exp(mat[i][j]+dp[i-1][k]+trans_mat[k][j]) for k in range(len(mat[0])))

    print(dp)
    return sum(dp[-1])


print(f3([[1,1,1],[1,1,1]],[[0.1,0.1,0,1],[0.1,0.1,0.1],[0.1,0.1,0.1]]))