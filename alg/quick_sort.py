def quick_sort(lis, r, l):
    if not lis or len(lis) <= 1:
        return
    if r<l:
        return

    i, j = r, l
    k = i

    while i < j:
        while i < j and lis[j] >= lis[k]:
            j = j - 1
        while i < j and lis[i] <= lis[k]:
            i = i + 1

        lis[i], lis[j] = lis[j], lis[i]
    lis[i], lis[k] = lis[k], lis[i]
    quick_sort(lis, r, i - 1)
    quick_sort(lis, i + 1, l)

lis=[3,2,1,3,5]


quick_sort(lis,0,len(lis)-1)