#head recursion
#job is frst done then fucntion is called again and again
count=0
def func(count):
    if count==4:
        return
    count+=1
    print(count)
    func(count)
func(0)

#tail recursion
#func is called until the condition fails and returns back to stack to give reverse output as head recursion
count=0
def func(count):
    if count==4:
        return 
    count+=1
    func(count)
    print(count)
func(0)

#recursion with parametre
#printing a number N times
def printf(x,n):
    if n==0:
        return
    print(x)
    n-=1
    printf(x,n)#or instead of n-=1 we can use printf(x,n-1) while calling
printf(12,4)

#printing 1 to n using recursion
def write(i,n):
    if i>n:    #Use i>n instead i==n because the last value would'nt print
        return
    print(i)
    write(i+1,n)
write(1,6)

#printing sum of n numbers

def sum_n(summ,i,n):
    if i>n:
        return summ
    summ=summ+i
    return sum_n(summ,i+1,n)
ans=sum_n(0,1,10)
print(ans)

#Using functional recursion
def func(n):
    if n==1:
        return 1
    else:
        return n+func(n-1)
ans=func(10)
print(ans)

#factorial of n numbers using fucntional recursion
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
ans=fact(4)    
print(ans)


#Reverse an array using recursion
nums=[2,5,6,1,6,8,4,7]
def rev_arr(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    rev_arr(nums,left+1,right-1)
    return nums
ans=rev_arr(nums,0,len(nums)-1)
print(ans)

#Reverse an part of the array using recursion
nums=[2,5,6,1,6,9,4,7]
def rev_array(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    rev_array(nums,left+1,right-1)
    return nums
answer=rev_array(nums,1,5)
print(answer)

#Reversing Normal logic
a=[4,1,5,9,0,7,2,6,3]
rev=[]
for i in range(len(a)-1,-1,-1):
    rev.append(a[i])
print(rev)

#Checking a string is palindrome or not
s=input("Enter a string>>")
def palindrome(s,l,r):
    if l>r:
        return True
    else:
        if s[l]!=s[r]:
            return False
        else:
             return palindrome(s,l+1,r-1)
ans=palindrome(s,0,len(s)-1)
print(ans)

