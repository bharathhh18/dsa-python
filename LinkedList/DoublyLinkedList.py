#Doubly linkedlist simple creating nodes
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
n1=node(10)
n2=node(12)
n3=node(15)
n4=node(18)
n5=node(21)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
head=n1
temp=head
while temp is not None:
    print(temp.val,end='<->')
    temp=temp.next
print("None")

class DoublyLinked:
    def __init__(self):
        self.head=None
    
    def insert_at_head(self,val):#o(1)
        newnode=node(val)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def append(self,val):#o(n)
        newnode=node(val)
        if self.head is None:
            self.head=newnode
        else:#We need else cause if when head none after being newnode as self.head it still traverse till end add it
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            newnode.prev=temp
            temp.next=newnode

    def insert_at_between(self,val,position):
        newnode=node(val)
        if position==0:
            self.insert_at_head(val)
            return
        count=0 #The node will be inserted after position if pos=3 node will be on 4th node if you want 3rd index start count with 1
        current=self.head
        while current is not None and count<position-1:
            current=current.next
            count+=1
        if current is None:
            print("Position out of bounds")
            return
        newnode.next=current.next
        newnode.prev=current
        if current.next:#Condition cause current may be last index
            current.next.prev=newnode
        current.next=newnode

    def delete(self,value):
        if self.head.val==value:
            self.head=self.head.next
        else:
            curr=self.head
            prev=None
            found=False
            while curr is not None:
                if curr.val==value:
                    found=True
                    break #IMP
                prev=curr
                curr=curr.next
            if found:
                prev.next=curr.next
            else:
                print("Node not found")
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.val,end=' <-> ')
            temp=temp.next
        print("None")
dll=DoublyLinked()
dll.insert_at_head(10)
dll.insert_at_head(15)
dll.append(18)
dll.append(25)
dll.insert_at_between(20,3)
dll.delete(15)
dll.append(15)
dll.display()

def reverse_dll(head):#Brute force solution where just changing value not link
    temp=head
    stack=[]
    while temp is not None:
        stack.append(temp.val)
        temp=temp.next
    temp=head
    for _ in range(len(stack)):
        e=stack.pop()
        temp.val=e
        temp=temp.next
    return head
temp=reverse_dll(dll.head)
while temp is not None:
    print(temp.val,end=' <-> ')
    temp=temp.next
print("None")

def op_reverse_dll(head):
    prev=None
    curr=head
    while curr is not None:
        front=curr.next
        curr.next=prev
        curr.prev=front
        prev=curr
        curr=front
    return prev
temp=op_reverse_dll(dll.head)
while temp is not None:
    print(temp.val,end=' <-> ')
    temp=temp.next
print("None")

#Remove all the occurence of target
def remove_occ(head,target):
    if head.next is None and head.val==target:
        return None
    while  head is not None and head.val==target:
        head=head.next
    curr=head
    prev=None
    while curr is not None:
        if curr.val!=target:
            prev=curr
            curr=curr.next
        else:
            prev.next=curr.next
            if curr.next:
                curr.next.prev=prev
            curr=curr.next #We should not move our prev if we move it would point to the deleted node
    return head
temp=remove_occ(dll.head,1)
while temp is not None:
    print(temp.val,end=' <-> ')
    temp=temp.next
print("None")
        
#Find the pairs which makes sum=k
#Brute force is just using two pointers 
def pairs(head,target):#Same like two sum #tc=o(n) sc=o(n)
    temp=head
    hash_map={}
    result=[]
    while temp is not None:
        need=target-temp.val
        if need in hash_map:
            result.append([need,temp.val])
        else:
            hash_map[temp.val]=0
        temp=temp.next
    return result
print(pairs(dll.head,7))
 
def op_pairs(head,target):#tc=o(2n) and sc=o(1)
    result=[]
    left=head
    right=head
    while right.next is not None:
        right=right.next
    while left is not None and right is not None and left.val<right.val:
        total_sum=left.val+right.val
        if total_sum>target:
            right=right.prev
        elif total_sum<target:
            left=left.next
        else:
            result.append([left.val,right.val])
            left=left.next #IMP dnt froget
            right=right.prev
    return result
print(op_pairs(dll.head,7))