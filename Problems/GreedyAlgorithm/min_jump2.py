#Minimun jumps to reach the end of the array using recursion
nums=[2,3,1,4,1,1,1,3]

def func(nums,index,jump):
    if index>=len(nums):
        return jump

    min_jump=float('inf')
    for i in range(1,nums[index]+1):
        min_jump=min(min_jump,func(nums,index+i,jump+1))
    return min_jump

print(func(nums,0,0))#Its brute force solution because its time complexity is O(n^n)