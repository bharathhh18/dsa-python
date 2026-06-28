#Selection sort
#Selects the smallest element in the unsorted part of the array and place it to its right place
nums=[4,1,5,9,0,7,2,6,3]
for i in range(0,len(nums)):
    min=i
    for j in range(i+1,len(nums)):
        if nums[j]<nums[min]:
            min=j
    nums[i],nums[min]=nums[min],nums[i]
print(nums)

#Bubble sort
#Sorts by comparing adjacent values
#time cpmplexity is O(n(n+1)/2)~~o(n^2)
a=[4,1,5,9,0,7,2,6,3]
n=len(a)
is_swap=False #for best case if array given is already sorted
for i in range(n-1,-1,-1):
    for j in range(0,i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            is_swap=True
        if is_swap==False:
            break
print(a)

#insertion sort
#comparing the element with prevoius index until the desired position would get
#Time complexity is o(n+(n+1)/2)~o(n^2)
a=[4,1,5,9,0,7,2,6,3]
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)

#Merge sort technique
#divide and merge technique
#Time complexity o(NlogN)
def merge_arr(left,right):#o(n)
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result
    
def merge_sort(arr):#o(logn)
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    right=merge_sort(right_arr)
    left=merge_sort(left_arr)
    return merge_arr(left,right)
a=[4,1,5,9,0,7,2,6,3]
ans=merge_sort(a)
print(ans)








