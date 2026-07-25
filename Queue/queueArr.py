#queue using arrays
class queue:
    def __init__(self):
        self.items=[]
        self.front=-1
        self.rear=-1

    def enque(self,n):
        if self.front==-1 and self.rear==-1:
            self.items.append(n)
            self.front+=1
            self.rear+=1
        else:
            self.rear+=1
            self.items.append(n)

    def deque(self):
        if len(self.items)==0:
            print("Queue is empty")
            return
        elif self.front==self.rear:
            self.items=[]
            self.front=-1
            self.rear=-1
        else:
            self.front+=1
        self.display()

    def display(self):
        if len(self.items)==0:
            print("Queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.items[i],end="\t")
            print()


#While dequeing we are just ignoring the front part and advancing it forward if we want to delete it from memory 
#We can use pop(0) which changes whole implementaion just try it once while practising
Queue=queue()
Queue.enque(10)
Queue.enque(12)
Queue.enque(19)        
Queue.display()
Queue.deque()
Queue.deque()
Queue.deque()