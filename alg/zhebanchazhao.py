# *coding:utf-8 *

def find(nums,x):
    if nums is None or len(nums)==0:
        return -1
    i,j=0,len(nums)-1

    while j>=i:
        mid = (i + j) // 2
        if x>nums[mid]:
            i=mid+1
        if x<nums[mid]:
            j=mid-1
        if x==nums[mid]:
            return mid
    return -1


def find_ruc(nums,i,j, x):
    if nums is None or len(nums) == 0:
        return -1
    if i<0 or i>len(nums)-1:
        return -1
    if j<0 or j>len(nums)-1:
        return -1
    mid = (i + j) // 2
    if x > nums[mid]:
        return find_ruc(nums,mid+1,j,x)
    if x < nums[mid]:
        return find_ruc(nums,i,mid-1,x)
    if x == nums[mid]:
        return mid
x=6
nums=[1,2,3,4,5]
print(find_ruc(nums,0,len(nums)-1,x))

def find2(nums,x):
    if nums is None or len(nums)==0:
        return -1
    if x<nums[0] or x>nums[-1]:
        return -1
    i,j=0,len(nums)-1

    while j>i:
        k = (x-nums[i])/(nums[j]-nums[i])
        mid = int(i+(j-i)*k)
        if x>nums[mid]:
            i=mid+1
        if x<nums[mid]:
            j=mid-1
        if x==nums[mid]:
            return mid
    return -1


print(find(nums,x))
print(find2(nums,x))
