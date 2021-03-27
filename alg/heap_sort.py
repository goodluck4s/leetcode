# -- coding: utf-8 --


def f(lis):
    if not lis:
        return
    build_heap(lis)

    for i in range(len(lis)-1,-1,-1): # 从后
        lis[0],lis[i] = lis[i],lis[0]
        totop(lis,i,0)



def build_heap(lis):
    for i in range(len(lis)//2-1,-1,-1):  # 从后
        totop(lis, len(lis), i)

def totop(lis,tail,i):
    index=i
    l = i*2+1
    r = i*2 +2

    if l<tail and lis[index]<lis[l]:
        index = l

    if r<tail and lis[index]<lis[r]:
        index = r

    if index!=i:
        lis[index],lis[i]=lis[i],lis[index]
        totop(lis,tail,index)


lis = [3, 2, 1,2]
f(lis)
print(lis)
