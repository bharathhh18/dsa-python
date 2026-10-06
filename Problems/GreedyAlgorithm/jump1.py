#Jump game!! Could i reach the end or not
nums=[3,2,1,4,0,2,1,5]
max_index=0
for i in range(0,len(nums)):
    if i>max_index:
       print("False")
    max_index=max(max_index,i+nums[i])
print("True")