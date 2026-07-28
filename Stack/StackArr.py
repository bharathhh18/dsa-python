#Stack using arrays
class Stack:
    def __init__(self):
        self.items=[]

    def push(self,n):
        self.items.append(n)

    def popp(self):
        if len(self.items)==0:
            print("stack is empty")
        x=self.items.pop()
        return x

    def display(self):
        for i in range(len(self.items)):
            print(self.items[i],end="\t")
        print()

    def topmost(self):
        if self.items[-1]==None:
            print("Stack is empty,no top element")
        return self.items[-1]
    
stack=Stack()
stack.push(10)
stack.push(19)
stack.display()
print(stack.topmost())
print(stack.popp())
stack.display()

#stack using queue
from collections import deque

class StackusingQueue:

    def __init__(self):
        self.queue=deque()

    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue.popleft()

    def top(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue[0]

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        return False
    
    def display(self):
        for num in self.queue:
            print(num)

q=StackusingQueue()

q.push(120)
q.push(90)
q.display()
q.pop()
print()
q.display()
