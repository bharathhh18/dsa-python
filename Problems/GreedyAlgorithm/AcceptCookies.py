#Accept cookies using greedy algorithm 
#Brute force solution by myself
greed=[2,6,8,1,4]
s=[4,2,7,1,2,3]
maxi=0
for num in greed:
    for anum in s:
        if anum >=num:
            maxi+=1
            s.remove(anum)
            break
print(maxi)

g=[2,6,8,1,4]
s=[4,2,7,1,2,3]

g.sort()
s.sort()
left=0
right=0
n=len(g)
m=len(s)
count=0

while left<n and right<m:
    if g[left]<=s[right]:
        count+=1
        left+=1
    right+=1
print(count)