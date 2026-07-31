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

#implimentation of stack using queue
class StackIUsingQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self,x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if len(self.stack1)==0:
            return "Stack is empty nothing to remove"
        poped=self.stack1.pop()
        return poped

    def display(self):
        if len(self.stack1)==0:
            return "Stack is empty"
        for num in self.stack1:
            print(num)
        print()

    def top(self):
        if len(self.stack1)==0:
            return "Stack is empty"
        return self.stack1[-1]

stack=StackIUsingQueue()

stack.push(10)
stack.push(12)
stack.display()
stack.pop()
stack.display()

#Implimenting stack using doubly linked list
class node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None


class stackUsingDll:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,val):
        newnode=node(val)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        elif self.head.next is None:
            self.head.next=newnode
            newnode.prev=self.head
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode

    def pop(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.display()

    def peek(self):
        if self.head is None:
            print("Node is empty")
        else:
            return self.tail.val

    def display(self):
        if self.head is None:
            print("Node is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.val,end="->")
                temp=temp.next
            print("None")

s=stackUsingDll()

s.push(10)
s.push(19)
s.push(20)
s.display()
s.pop()
print(s.peek())

#Implementing queue using doubly linked list
class node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None


class QueueUsingDll:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,val):
        newnode=node(val)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        elif self.head.next is None:
            self.head.next=newnode
            newnode.prev=self.head
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")    
        elif self.head.next is None:
            self.head,self.tail=None,None
        else:
            temp=self.head.next
            self.head.next.prev=None
            self.head.next=None
            self.head=temp
    def peek(self):
        if self.head is None:
            print("Queue is empty")
            return
        else:
            return self.head.val
    def display(self):
        if self.head is None:
            print("Node is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.val,end="->")
                temp=temp.next
            print("None")

s=QueueUsingDll()

s.enqueue(10)
s.enqueue(19)
s.enqueue(20)
s.display()
s.dequeue()
s.display()
print(s.peek())