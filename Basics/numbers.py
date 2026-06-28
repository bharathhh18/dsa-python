#Count digits
count=0
num=int(input("Enter a number>>"))
while num>0:
    lnum=num%10
    count+=1
    num=num//10
print(count)

#Extracting last digits
num=5609
while num!=0:
    lnum=num%10
    num=num//10
    print(lnum)

#Armstrong number
num=int(input("Enter a number>>"))
temp=num
def count(num):
    countt=0
    while num>0:
        countt+=1
        num//=10
    return countt
#it took so long brooo
sum=0
digits=count(num)
while num>0:
    lnum=num%10
    sum+=lnum**digits
    num//=10
if sum==temp:
    print("Armatrong")
else:
    print("Not a armstrong")

#Finding Factors of a number
num=int(input("Enter the number>>")) 
print("The factors of number are")
for i in range(1,(num//2)+1):# +1 because num//2 will be the limit it wont consider num//2
    if num%i==0:
        print(i,end="\t")
print(num)

#Fibanacci number
# 0 1 1 2 3 5 8 13 21
#f1 2 3 4 5 6 7 f8 f9
#Basically fib(5) if fib(4)+fib(3) 
#Fibanacci number using recursion
def fib(num):
    if num==0 or num==1:
        return num
    return fib(num-1)+fib(num-2)
ans=fib(6)
print(ans)

#Palindrome number
num=int(input("Enter a number>>"))
temp=num
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num//=10
if rev==temp:
    print("Its an palindrome nnumber")
else:
    print("Its not an palindrome number")

    
