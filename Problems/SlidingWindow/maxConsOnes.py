#Maximium consecutive ones where k number of 0 are allowed in sequance
#Brute force solution
nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
maxi=0
n=len(nums)
for i in range(0,n):
    zeros=0
    for j in range(i,n):
        if nums[j]==0:
            zeros+=1
        if zeros>k:
            break
        maxi=max(maxi,j-i+1)
print(maxi)

#Better solution using sliding windows
nums=[1,1,1,0,0,0,1,1,1,1,0] #o(2n)
left=0
right=0
zeros=0
maxi=0
k=2
n=len(nums)
while right<n:
    if nums[right]==0:
        zeros+=1
    while zeros>k:
        if nums[left]==0:
            zeros-=1
        left+=1
    if zeros<=k:
        maxi=max(maxi,right-left+1)
    right+=1
print(maxi)

#Optimal solution
nums=[1,1,1,0,0,0,1,1,1,1,0]
left=0
right=0
zeros=0
k=2
maxi=0
n=len(nums)
while right<n:
    if nums[right]==0:
        zeros+=1
    if zeros>k:
        if nums[left]==0:
            zeros-=1
        left+=1
    if zeros<=k: #Dryrun if you get confused
        maxi=max(maxi,right-left+1)
    right+=1
print(maxi)