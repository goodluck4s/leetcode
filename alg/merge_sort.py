# -- coding: utf-8 --


def f(lis):
    if len(lis) <= 1:
        return lis

    mid = len(lis) // 2
    a = f(lis[:mid])
    b = f(lis[mid:])
    return merge(a, b)


def merge(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    if i == len(a):
        res += b[j:]
    if j == len(b):
        res += a[i:]
    return res


lis = [3, 2, 1]
lis = f(lis)
print(lis)
