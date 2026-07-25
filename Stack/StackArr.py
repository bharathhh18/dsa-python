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
