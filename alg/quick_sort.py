# -- coding: utf-8 --


def f(lis,l,r):
    if not lis:
        return
    if l>r:
        return
    i,j = l,r
    k = lis[l]
    while i<j:
        while i < j and lis[j] >= k:
            j -= 1
        while i<j and lis[i]<=k:
            i+=1
        lis[i],lis[j] = lis[j],lis[i]
    lis[i], lis[l] = lis[l], lis[i]

    f(lis,l,i-1)
    f(lis,i+1,r)

lis=[3,2,1,2,0,5,1,23,14,0]
f(lis,0,len(lis)-1)
print(lis)



def quick_sort(nums,l,r):
    if not nums:
        return
    if l>r:
        return
    i,j = l,r
    k = nums[l]
    while i<j:
        while i<j and nums[j]>=k:
            j-=1
        while i < j and nums[i] <= k:
            i+=1

        nums[i],nums[j] = nums[j],nums[i]

    nums[i],nums[l] = nums[l],nums[i]

    quick_sort(nums,l,i-1)
    quick_sort(nums,i+1,r)

nums = [4,3,2,1,0]
print(quick_sort(nums,0,len(nums)-1))
print(nums)


