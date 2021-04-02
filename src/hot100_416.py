
def func(n):

    res=[]
    tmp=[]

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

print(func(3))