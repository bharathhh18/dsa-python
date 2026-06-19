nums=[2,4,6,7,9,11,18,19]
def binarysearch(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
ans=binarysearch(nums,18)
print(ans)

#Using recursion
nums=[2,4,6,7,9,11,18,19]
def binarysearch(nums,low,high,target):
    if low>high:
        return -1 
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif target<nums[mid]:
        return binarysearch(nums,low,mid-1,target)
    else:
        return binarysearch(nums,mid+1,high,target)
ans=binarysearch(nums,0,len(nums)-1,18)
print(ans)

#Smallest index such that arr[i]>=target 
arr=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13] #Lowerbound
lower_bound=len(arr)
low=0
high=len(arr)-1
target=1
while low<=high:
    mid=(low+high)//2
    if arr[mid]>=target:
        lower_bound=mid
        high=mid-1
    else:
        low=mid+1
print(lower_bound)

#Smallest index such that arr[i]>target
arr=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13] #Upperbound
n=len(arr)
ub=n
low=0
high=n-1
target=1
while low<=high:
    mid=(low+high)//2
    if arr[mid]>target:
        ub=mid
        high=mid-1
    else:
        low=mid+1
print(ub)
#If target is 1 lower bound gives where the 1 starts and upper bound gives where the 1 ends

#Search insert question
arr=[1,3,4,5,8,9,14,15,19,20,21]
n=len(arr)
target=2
low=0
high=n-1
lb=n
while low<=high:
    mid=(low+high)//2
    if arr[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(f"Target should appear in index {ub}")