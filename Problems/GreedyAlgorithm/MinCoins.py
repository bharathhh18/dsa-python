#Maximum number of coins 
# Find the minimum coins needed to make the given amount
coins=[1,2,5,10,20,50,100,500,2000]
coin=47
n=len(coins)
result=[]
for i in range(n-1,-1,-1):
    while coin>=coins[i]:
        result.append(coins[i])
        coin-=coins[i]
print(result)