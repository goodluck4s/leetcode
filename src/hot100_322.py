# 322  零钱兑换  用[2,5]  兑6块钱



# 回溯
qian = [1,5,11]
def f(n):
    if n<0:
        return 9999
    if n==0:
        return 0
    return min(f(n-11)+1,f(n-5)+1,f(n-1)+1)

# 动归   自下而上
qian = [5,11]
def f(n):
    if n<=0:
        return 0
    maxint = 9999
    cache = [maxint]*(n+1)
    cache[0]=0
    for i in range(1,n+1):
        for j in qian:
            cache[i] = min(cache[i],cache[i-j]+1 if i-j >=0 else maxint)
    return cache[-1] if cache[-1]<maxint else -1





