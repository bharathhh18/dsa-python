bills=[5,5,5,10,20]

#Leetcode 806
def Lemonade_change(bills):
    five=0
    ten=0
    for i in range(0,len(bills)):
        if bills[i]==5:
            five+=1
        elif bills[i]==10:
            if five>=1:
                ten+=1
                five-=1
            else:
                return False
        else:
            if ten>=1 and five>=1:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True

ans=Lemonade_change(bills)
print(ans)