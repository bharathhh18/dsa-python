#Maximum points can be obtained
nums=[1,2,3,4,5,6,1]
k=3
n=len(nums)
right_sum,left_sum=0,0
for i in range(0,k):
    left_sum+=nums[i]
maxi=left_sum
right_ind=n-1   
for i in range(k-1,-1,-1):
    left_sum-=nums[i]
    right_sum+=nums[right_ind]
    maxi=max(maxi,right_sum+left_sum)
    right_ind-=1
print(maxi)