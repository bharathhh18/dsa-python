def converttodecimal(num:str)->int:
    ans=0
    index=len(num)-1
    power=0
    while index>=0:
        if num[index]=="1":
            ans+=(2**power)
        power+=1
        index-=1
    return ans
    

binary="1101"
ans=converttodecimal(binary)
print(ans)

num=2
def converttobinary(num:int)->str:
    result=""  #o(logN)
    while num>0:
        if num%2==1:
            result+="1"
        else:
            result+="0"
        num=num//2
    result=result[::-1]
    return result
ans=print(converttobinary(num))

#left shift
num=1
num=num<<3
print(num)

#Right shift
num=8
num=num>>2
print(num)

#Ith bit is set or not
num=13
i=1
if(num & 1<<i!=0):
    print(True)
else:
    print(False)
#Using Right shift
num=13
i=1
if(num<<i & 1)==1:
    print(True)
else:
    print(False)

#Set theh ith bit
num=9
i=2
num=(num | (1<<i))
print(num)

#Clear the ith bit
num=13
i=2
num=num & ~(1<<i)
print(num)

#Toggle the ith bit
num=13
num=num ^ (1<<i)
print(num)

#Remove the rigthmost set bit
num=16
num=num & (num-1)

#Check if the number is power of 2
num=16
if (num & num-1)==0:#Removing right most bit gives 0 
    print(True)
else:
    print(False)
#Brute
num=28
while num>2:
    num=num//2
if num==2:
    print(True)
else:
    print(False)

#Find the number which appears only once in array
#Brute use dictionary
arr=[5,1,3,3,7,1,7]
ans=0
for num in arr:
    ans=ans^num
print(ans)

#Give all the subset possible in array
arr=[1,2,3]
result=[]
n=len(arr)
total_subset=1<<n
for num in range(0,total_subset):#O(2^N * N)
    lst=[]
    for i in range(0,n):
        if (num & 1<<i)!=0:
            lst.append(arr[i])
    result.append(lst)
print(result)