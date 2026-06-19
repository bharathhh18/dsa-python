#Max consecutive numbers in array
arr=[1,99,101,98,2,5,3,100]
n=len(arr)
max_count=0
hash_map={}
for i in range(0,n):
    hash_map[arr[i]]=i
for i in range(0,n):
    count=1
    temp=arr[i]+1
    while temp in hash_map:
        count+=1
        temp+=1
    temp=0
    if count>max_count:
        max_count=count
print(max_count)

#Max consecutive numbers in array
arr=[1,99,101,102,98,2,5,3,100]
srt_arr=sorted(arr)
print(srt_arr)
#[1, 2, 3, 5, 98, 99, 100, 101,102]
prev_num=float("-inf")
count=0
long_count=0
i=0
while i<len(srt_arr):#o(2n)~0=o(n) one N for sorting one for traversing
    if srt_arr[i]-prev_num==1:
        count+=1
        prev_num=srt_arr[i]
        i+=1
    else:
        count=1
        prev_num=srt_arr[i]
        i+=1
    if count>long_count:
        long_count=count
print(count)

#Rotate an array by 90 degree
nums=[[2,3,4],[6,7,8],[9,8,0]]
rows=len(nums)
cols=len(nums[0])
result=[[0,0,0],[0,0,0],[0,0,0]]#result[[0 for _ in range(rows)] 0 for _ in range(rows)] using list comprehension
for i in range(rows):
    for j in range(cols):
        print(nums[i][j],end=' ')
    print()
for i in range(rows):
    for j in range(cols):
        result[j][(rows-1)-i]=nums[i][j]
print(result)
#tc -> o(n^2)
#sc -> o(n^2)
 
#optimal solution
matrix=[[1,2,3],[4,5,6],[7,8,9]]
n=len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j],end=' ')
    print()
print()
#Now we are going to transpose it which means rows to column and column to row
#If any confusion occurs refer "transpose2Darray" screenshot
for i in range(0,n-1):
    for j in range(i+1,n):#Refer screenshot for parameter clarification
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(0,n):
    matrix[i].reverse()
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j],end=' ')
    print()
print()
#tc -> o(n^2)+o(n^2)
#sc -> o(1)

#Print a Spiral matrix       
#1  2  3  4  5  6
#20 21 22 23 24 7
#19 32 33 34 25 8 
#18 31 36 35 26 9 
#17 30 29 28 27 10
#16 15 14 13 12 11
#we should iterate left down right up manner
matrix=[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
n=len(matrix)
result=[]
left,top=0,0
right,bottom=n-1,n-1
while top<=bottom and left<=right:
    for i in range(left,right+1):
        result.append(matrix[left][i])
    top+=1
    for i in range(top,bottom+1):
        result.append(matrix[i][right])#i takes from 1 cause the loop is from top to bottom so i would initially top value
    right-=1
    if top<=bottom: #It applies when the matrix is one row after first for loop the top value exceeds the bottom so this would again print the same line if the condition was not there
        for i in range(right,left-1,-1): #left-1 means 0-1=-1 where -1 would be excluded until 0 is iterated
            result.append(matrix[bottom][i])
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        left+=1
print(result)

#3 sum problem
arr=[-1,0,1,2,-2,-4]#using 3 pointers
my_set=set()
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==0:
                temp=[arr[i],arr[j],arr[k]]
                temp.sort()
                my_set.add(tuple(temp))#Cause we cant add list into set
print([list(ans) for ans in my_set])#List comprehension
#TC booooommm!!!! btw its brute force solution
#SC o(no of triplets)
#Now with o(n^2)
#SC o(n)+0(no of triplets)
arr=[-1,0,1,2,-2,-4]
n=len(arr)
hash_map={}
result=set()
for i in range(0,n):
    my_set=set()    #We cant use dictionary here cause when i and j are in somwhere middle -(arr[i]+arr[j]) may give the number which occurs before arr[i] or arr[j] so we have to change my_set on every i ietartion
    for j in range(i+1,n):
        third_number=-(arr[i]+arr[j])
        if third_number in my_set:
            temp=[arr[i],arr[j],third_number]
            temp.sort()
            result.add(tuple(temp))
        else:
            my_set.add(arr[j])
print([list(ans) for ans in result])

#The three sum problem cant be solved in o(n^2) TC so we have to decrease the space complexity
#So the my_set which was taking o(n)SC we are removing with to decraese the TC
arr=[-1,0,1,2,-2,-4]
arr.sort()
print(arr)
result=[]
n=len(arr)
for i in range(n):
    if i!=0 and arr[i]==arr[i-1]:
        continue
    j=i+1
    k=n-1
    while j<k:
        total_sum=arr[i]+arr[j]+arr[k]
        if total_sum<0:
            j+=1   #We are trying to come close to 0
        elif total_sum>0:
            k-=1
        else:
            temp=[arr[i],arr[j],arr[k]]
            result.append(temp)
            j+=1
            k-=1
            while j<k and arr[j]==arr[j-1]:
                j+=1
            while j<k and arr[k]==arr[k-1]:
                k-=1
print(result)

arr=[-1,0,1,2,-2,-4]
n=len(arr)
result=[]
arr.sort()
for i in range(n):
    if i!=0 and arr[i]==arr[i-1]:#i!=0 cause when i=0 it checks arr[0]==arr[-1] which means the last element
        continue #This skips the next code and directly jumps to the for loop again
    j=i+1
    k=n-1
    while j<k:
        total_sum=arr[i]+arr[j]+arr[k]
        if total_sum<0:
            j+=1
        elif total_sum>0:
            k-=1
        else:
            temp=[arr[i],arr[j],arr[k]]
            result.append(temp)
            j+=1
            k-=1
            while j<k and arr[j]==arr[j+1]:#We should increment soon triplet is found this part only increments when duplicates are found
                j+=1
            while j<k and arr[k]==arr[k-1]:
                k-=1
print(result)




 


    

    



        


