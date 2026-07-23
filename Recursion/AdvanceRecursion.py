#Generate all the possible subsequances
arr=[1,2,3]
result=[]
def solve(index,subset):
    if index>=len(arr):
        result.append(subset.copy())
        return
    subset.append(arr[index])
    solve(index+1,subset)
    subset.pop()
    solve(index+1,subset)
solve(0,[])
print(result)

#Generate all the subsequances making sum=k       
arr=[5,4,9]
result=[]
target=9
def solve(index,total,subset):
    if total==target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if index>=len(arr):
        return
    subset.append(arr[index])
    total=total+arr[index]
    solve(index+1,total,subset)
    e=subset.pop()
    total-=e
    solve(index+1,total,subset)
solve(0,0,[])
print(result)

#Check if subsequances making sum=k exist or not
arr=[5,9,4]
result=[]
target=9
def solve(index,total,subset):
    if total==target:
        result.append(subset.copy())
        return True
    elif total>target:
        return False
    if index>=len(arr):
        return False
    subset.append(arr[index])
    total+=arr[index]
    pick=solve(index+1,total,subset)
    if pick==True:
        return
    e=subset.pop()
    total-=e
    not_pick=solve(index+1,total,subset)
    return not_pick
solve(0,0,[])
print(result)

#Count the number of subsequances which makes sum=k
arr=[5,4,9]
target=9
def solve(index,total):
    if total==target:
        return 1
    elif total>target:
        return 0
    if index>=len(arr):
        return 0
    sum=total+arr[index]
    pick=solve(index+1,sum)
    sum=total
    not_pick=solve(index+1,sum)
    return pick+not_pick
print(solve(0,0))

#Generate all the binary numbers which doesnt have 1 on adjacent
n=4
numbers=[0]*n
result=[]
def solve(index,flag,numbers,result):
    if index>=len(numbers):
        result.append("".join(numbers))
        return
    numbers[index]="0"
    solve(index+1,True,numbers,result)
    if flag==True:
        numbers[index]="1"
        solve(index+1,False,numbers,result)
        numbers[index]="0"
solve(0,True,numbers,result)
print(result)

#Combitional Sum 1
arr=[2,3,6,7]
result=[]
def func(index,total,subset,arr,target,result):
    if total==target:
        result.append(subset.copy())
        return
    elif total>target:
        return
    if index>=len(arr):
        return
    subset.append(arr[index])
    summ=total+arr[index]
    func(index,summ,subset,arr,target,result)
    summ=total
    subset.pop()
    func(index+1,summ,subset,arr,target,result)
func(0,0,[],arr,7,result)
print(result)


#Combinational summ 2
#Duplicates may exist in the array,result should not contain duplicates ,pick not pick stratery
arr=[1,1,2,1,2]#brute
result=set()
def func(index,total,subset,arr,target,result):
    if total==target:
        subset.sort()
        result.add(tuple(subset.copy()))
        return
    elif total>target:
        return
    if index>=len(arr):
        return
    subset.append(arr[index])
    summ=total+arr[index]
    func(index+1,summ,subset,arr,target,result)
    subset.pop()
    summ=total
    func(index+1,summ,subset,arr,target,result)
func(0,0,[],arr,4,result)
print(list(result))

#optimal
arr=[1,1,1,2,2]
target=4
result=[]
def func(index,total,subset):
    if total==0:
        result.append(subset.copy())
        return
    if index>=len(arr):
        return
    if total<0:
        return
    for i in range(index,len(arr)):
        if i>index and arr[i]==arr[i-1]:
            continue
        subset.append(arr[i])
        summ=total-arr[i]
        func(i+1,summ,subset)
        subset.pop()
func(0,4,[])
print(result)

#Subset sum 
arr=[5,4,9]#Brute force approach
result=[]
summ=[]
def subset_sum(index,total,subset):
    if index==len(arr):
        result.append(subset.copy())
        summ.append(total)
        return
    subset.append(arr[index])
    summm=total+arr[index]
    subset_sum(index+1,summm,subset)
    subset.pop()
    subset_sum(index+1,total,subset)
subset_sum(0,0,[])
print(result)
print(summ)

#Subset sum optimmal approach
arr=[5,4,9]
result=[]
def subset_sum_optimal(index,total):
    if index>=len(arr):
        result.append(total)
        return
    summ=total+arr[index]
    subset_sum_optimal(index+1,summ)
    summ=total
    subset_sum_optimal(index+1,summ)
subset_sum_optimal(0,0)
print(result)


#combinational sum 3
result=[]
target=8
k=2
def func(index,total,subset):
    if total==target and len(subset)==k:
        result.append(subset.copy())
        return
    if total>target and  len(subset)>k:
        return 
    for i in range(index,10):
        summ=total+i
        subset.append(i)
        func(i+1,summ,subset)
        subset.pop()      
func(1,0,[])
print(result)

#Letter combination of a phone number
char_set={
"2":"abc",
"3":"def",
"4":"ghi",
"5":"jkl",
"6":"mno",
"7":"pqrs",
"8":"tuv",
"9":"wxyz"
}
result=[]
digits=str(input("Enter the digit:"))
def func(index,subset):
    if index>=len(digits):
        result.append("".join(subset))
        return
    for ch in char_set[digits[index]]:
        subset.append(ch)
        func(index+1,subset)
        subset.pop()
func(0,[])
print(result)

#N Queens 
class queen:
    def solve(self,col,board,ans,n):# Any doubt refer code and debug video 
        
        if col==n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe(row,col,n,board):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                self.solve(col+1,board,ans,n)
                board[row]=board[row][:col]+"."+board[row][col+1:]
        return ans


    def isSafe(self,row,col,n,board):
        duprow=row
        dupcol=col
        while row>=0 and col>=0:
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1
        row=duprow
        col=dupcol
        while col>=0:
            if board[row][col]=="Q":
                return False
            col-=1
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=="Q":
                return False
            row+=1
            col-=1
        return True

solution=queen()
n = 4
board = ["." * n for _ in range(n)]
ans = []

solution.solve(0, board, ans, n)
print(ans)

#TC->O(N!*N)
#SC->o(n^2)

#N-Queen Optimal Solution 
class solution:#refer the same video if you have doubt
    def solve(self,col,board,n,ans,left,Ud,lD):
        if col==n:
            ans.append(list(board))
            return
        for row in range(n):
            if(left[row]==0 and
               Ud[row+col]==0 and
               lD[(n-1)+(row-col)]==0
            ):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                left[row]=1
                Ud[row+col]=1
                lD[(n-1)+(row-col)]=1
                self.solve(col+1,board,n,ans,left,Ud,lD)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                left[row]=0
                Ud[row+col]=0
                lD[(n-1)+(row-col)]=0

    def SolveQueen(self,n:int)->list[list[str]]:
        ans=[]
        board=["."*n for _ in range(n)]
        left=[0]*n
        Ud=[0]*(2*n-1)
        lD=[0]*(2*n-1)
        self.solve(0,board,n,ans,left,Ud,lD)
        return ans
answer=solution()
print(answer.SolveQueen(4))
#TC->O(N!) because not isSafe traversal we would get in O(n)
#SC->O(n^2)

