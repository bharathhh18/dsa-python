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