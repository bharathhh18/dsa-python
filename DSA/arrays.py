#Check if an array is sorted or not
a=[0,1,2,3,4,5]
b=[7,6,2,4,8]
def srt(a):
    n=len(a)
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            return False
    return True
ans=print(srt(a))
ans=print(srt(b))

#Remove duplicate values from a sorted array
#And return the number of Unique elements
a=[1,1,1,2,3,4,4,7,9,9,10]
freq_map={}
for i in range(len(a)):#o(n)
    if i not in freq_map:
        freq_map[a[i]]=0
print(freq_map)
j=0
for key in freq_map:#o(n) total 0=o(2n)~o(n)
    a[j]=key
    j+=1
print(j)

#Remove duplicate values from a sorted array using two pointers
#And return the number of Unique elements
a=[1,1,1,2,3,4,4,7,9,9,10]
n=len(a)
i=0
j=i+1
while j<n:
    if a[i]!=a[j]:   #When You get stuck take a simplier version and trace it!!
        i+=1
        a[i],a[j]=a[j],a[i]
        j+=1
    else:
        j+=1
print(a)
print(i+1) #We should return i+1 because indexing start with 0 rightt while pointing a number it is actually one number behind

#Rotating an array by 1 place
#a=[4,1,5,9,0,7,2,6,3] rorating 1 means array becomes a=[3,4,1,5,9,0,7,2,6]
a=[4,1,5,9,0,7,2,6,3]
n=len(a)
temp=a[n-1]
for i in range(n-2,-1,-1):
    a[i+1]=a[i]
a[0]=temp
print(a)

#Rotatig an array by k places
a=[4,1,5,9,0,7,2,6,3] 
n=len(a)
k=11
for j in range(k):
    temp=a[n-1]
    for i in range(n-2,-1,-1):
        a[i+1]=a[i]
    a[0]=temp
print(a)

#Using python libraries
a=[4,1,5,9,0,7,2,6,3]
n=len(a)
k=2
rotation=k%n
print(rotation)#rotating k=10 times is equal to rotating 1 time(when n=9)so when rotation takes place for n times that becomes the same array before rotation
for _ in range(rotation): # i is no use in loop so we can use _ instead
    e=a.pop()
    a.insert(0,e)
print(a)

#Move 0's to the end of the list
nums=[1,0,2,3,0,0,4,9,0]
temp=[]
n=len(nums)
for i in range(0,n):#o(n)
    if nums[i]!=0:
        temp.append(nums[i])
ln=len(temp)
for i in range(0,ln):# 0 to ln and ln to n that means whole nums array o(n)
    nums[i]=temp[i]
for i in range(ln,n):
    nums[i]=0
print(nums)
#Total o(2n)~o(n) space complexity o(n)
#Optimal solution wtih sc with o(1)
nums=[1,0,2,3,0,0,4,9,0]
i=0
for j in range(len(nums)):#Once dry run if you feel confused
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
print(nums)

#Merge two sorted array without duplicates
nums1=[1,1,1,2,3,4]
nums2=[2,3,3,3,4,4,4,5,5]
result=[]
i,j=0,0
n,m=len(nums1),len(nums2)
while i<n and j<m:
    if nums1[i]<nums2[j]:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
    else:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1
while i<n:
    if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
    i+=1
while j<m:
    if len(result)==0 or result[-1]!=nums2[j]:
        result.append(nums2[j])
    j+=1
print(result)

#Find the missing number in an array
#so the idea is i loop run taking the value upto len(arr)
#And j traverses the array and if we get value in the array while traversing j gets 0 checking again array i+=1
arr=[0,4,2,5,3,1]

def miss_num(arr):
    n=len(arr) #I did it myself
    i=0
    j=0
    while j<n:
        if i==arr[j]:
            j=0
            i+=1
        else:
            j+=1
    return i
#o(n^2)

#More simpler way 
for i in range(0,len(arr)+1):
    if i not in arr:
        print(i)
#o(n^2)
ans=miss_num(arr)
print(ans)
#o(3n)
arr=[0,4,2,5,1]
hash_map={0:0,1:0,2:0,3:0,4:0,5:0}
for i in range(0,len(arr)):
    hash_map[arr[i]]=1
for k,v in hash_map.items():
    if v==0:
        print(k)


#Optimal way
arr=[0,4,2,5,1]
n=len(arr)
total_sum=n*(n+1)/2#Formula for n natural numbers
summ=0
for i in range(0,n):
    summ=summ+arr[i]
print(int(total_sum-summ))

#Find the maximum conseccutive value
arr=[1,1,0,1,1,1,1,0,0,1,1,1,1,1]
n=len(arr)
max_count=0
i=0
while i<n:
    count=0
    while i<n and arr[i]==1 :
        count+=1
        i+=1
    if count>max_count:
        max_count=count
    i+=1
print(max_count)
    

#Two sum problem
arr=[3,6,7,0,5,7,9]        #hash_map[need] gives value whereas need gives key
def two_sum(arr,target):
    hash_map={}
    for i in range(len(arr)):
        need=target-arr[i]
        if need in hash_map:
            return hash_map[need],i
        else:
            hash_map[arr[i]]=i
ans=two_sum(arr,12)
print(ans)

#Find the maximum subarray sum
arr=[-2,1,-3,4,-1,2,1,-5,4]
maxi=float("-inf")
print(maxi)
for i in range(len(arr)):#o(n(n+1)/2)~o(n^2)
    total=0
    for j in range(i,len(arr)):
        total=total+arr[j]
        if total>maxi:
            maxi=total
print(maxi)

#Optimal solution
arr=[-2,1,-3,4,-1,2,1,-5,4]#Its based on something kadane algorithm
maxi=float("-inf")#Which says if total value becomes <0 we shall make it 0
print(maxi)
for i in range(len(arr)):#o(n(n+1)/2)~o(n^2)
    total=total+arr[i]
    if total>maxi:
        maxi=total
    if total<0:
        total=0
print(maxi)

#Best time to buy and sell stocks
arr=[7,2,1,5,6,4,8]
maxi_profit=0
for i in range(len(arr)):
    total=0
    for j in range(i+1,len(arr)):
        total=arr[j]-arr[i]
        maxi_profit=max(total,maxi_profit)
print(maxi_profit)

#Optimal solution
#Try to find min and the max num occuring after the 
prices=[7,2,1,5,6,4]
min_price=prices[0]
max_price=float("-inf")
for i in range(1,len(prices)):
    if prices[i]<min_price:
        min_price=prices[i]
    else:
        if prices[i]-min_price>max_price:
            max_price=prices[i]-min_price
        #max_price=max(max_price,prices[i]-min_price) another method
print(max_price)

#Rearrange the elements by sign
arr=[5,10,-3,-1,-10,6] #We should return [5,-3,10,-1,6,-10]
pos=[]
neg=[]
for i in range(len(arr)):
    if arr[i]<0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])
for i in range(len(pos)):
    arr[2*i]=pos[i]        #When i=0 we should update in 0 and 1 index
    arr[(2*i)+1]=neg[i]    #Same when i=1 we should update 2 and 3 index so we got a formula
print(arr) #o(n+n/2)

#Rearrange the elements by sign
arr=[5,10,-3,-1,-10,6] #We should return [5,-3,10,-1,6,-10]
result=[0]*len(arr)
p=0
n=1
for i in range(len(arr)):
    if arr[i]<0:
        result[n]=arr[i]
        n+=2
    else:
        result[p]=arr[i]
        p+=2
print(result)







    







     











