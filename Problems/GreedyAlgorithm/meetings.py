#N meeting in the room
start=[1,3,0,5,8,5]
end=[2,4,6,7,9,9]

class Meeting:
    def __init__(self,start,end,position):
        self.start=start
        self.end=end
        self.position=position

meet=[Meeting(start[i],end[i],i+1) for i in range(len(start))]
meet.sort(key=lambda x:(x.end,x.start))

result=[1]
count=1
last_time=meet[0].end
for i in range(1,len(start)):
    if meet[i].start>last_time:
        count+=1
        result.append(i+1)
        last_time=meet[i].end
print(result)
print(count)