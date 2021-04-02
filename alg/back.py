# -- coding: utf-8 --


# 枚举所有子串
def func1(lis):
    if not lis:
        return []

    res = []
    tmp = []

    def f(i):
        if i == len(lis):
            res.append(tmp[:])
            return
        for j in range(i, len(lis)):
            tmp.append(lis[i:j + 1])
            f(j + 1)
            tmp.pop()
    f(0)
    return res

print(func1("abcd"))
print(func1([1,2,3]))

# 枚举二进制组合  进而是全部的组合
def func2(n):
    if n==0:
        return None
    res=[]
    tmp = []

    def f():
        if len(tmp)==n:
            res.append(tmp[:])
            return
        for i in [0,1]:
            tmp.append(i)
            f()
            tmp.pop()

    f()
    return res

print(func2(3))


# 枚举所有
def func3(nums,k):
    res=[]
    tmp=[]

    def f(b):
        a = sum(tmp)
        if a >= k:
            if a == k:
                res.append(tmp[:])
            return

        for i in range(b,len(nums)):
            tmp.append(nums[i])
            f(i+1)
            if tmp:
                tmp.pop()

    f(0)
    return res

print(func3([1,2,3,4,5,6,7],8))

