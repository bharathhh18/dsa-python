# #2 3 4 
# #6 7 8
# #9 8 0
nums=[[2,3,4],[6,7,8],[9,8,0]]
rows=len(nums)
cols=len(nums[0])
for i in range(rows):
    for j in range(cols):
        print(nums[i][j],end=' ')
    print("\n")
#Sum of the elements
summ=0
for i in range(rows):
    for j in range(cols):
        summ+=nums[i][j]
print(summ)

#Printing upper triangle
rows=len(nums)
cols=len(nums[0])
for i in range(rows):
    for j in range(cols):
        if j>=i:
            print(nums[i][j],end=' ')
        else:
            print("*",end=' ')
    print()

#Print lower triangle
rows=len(nums)
cols=len(nums[0])
for i in range(rows):
    for j in range(cols):
        if j<=i:
            print(nums[i][j],end=' ')
        else:
            print("*",end=' ')
    print()


