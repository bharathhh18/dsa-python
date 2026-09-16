#Fractional knapsack problem using greedy algorithm
arr=[(100,20),(60,10),(100,50),(200,50)]


arr.sort(key=lambda x:x[0]/x[1],reverse=True)

bag_threshold=90
current_weight=0
final_value=0

for value,weight in arr:
    if current_weight+weight <= bag_threshold:
        current_weight+=weight
        final_value+=value
    else:
        remain=bag_threshold-current_weight
        cost=(value/weight)*remain
        final_value+=cost
        break
print(final_value)