#How to write a linked list in code
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
node1=node(5)
node2=node(10)
node3=node(11)
node4=node(13)
node1.next=node2
node2.next=node3
node3.next=node4
print(node2.next.val)

#Append using methods
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SinglyLinked:
    def __init__(self):
        self.head=None
    def append(self,val):
        new_node=node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node
    def display(self):
        if self.head==None:
            print("Single linked list is empty")
        else:
            curr=self.head
            while curr!=None:
                print(curr.val,end="->")
                curr=curr.next
            print("None")
    def insert_at_loc(self,val,position):
        new_node=node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            count=0
            curr=self.head
            prev=None
            while count<position and curr!=None:
                prev=curr
                curr=curr.next
                count+=1
            prev.next=new_node
            new_node.next=curr
        self.display()
    def delete(self,value):
        temp=self.head
        if temp.val==value:
            self.head=temp.next
        else:
            prev=None
            found=False
            while temp!=None:
                if temp.val==value:
                    found=True
                    break
                prev=temp
                temp=temp.next
            if found:
                prev.next=temp.next
            else:
                print("Node not found")
        self.display()

linkedlist=SinglyLinked()
linkedlist.append(9)
linkedlist.append(19)
linkedlist.append(10)
linkedlist.append(18)
linkedlist.append(89)
linkedlist.display()
linkedlist.insert_at_loc(15,3)
linkedlist.delete(19)
linkedlist.delete(9)
linkedlist.delete(21)

def middle(head):
    count=0
    temp=head
    while temp!=None:
        count+=1
        temp=temp.next
    temp=head
    for _ in range(0,count//2):
        temp=temp.next
    print(temp.val)
middle(linkedlist.head)

def optimal_middle(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    print(slow.val)
optimal_middle(linkedlist.head)

#Reverse a linked list(Brute)
def reverse(head):#o(2n)~o(n)
    temp=head
    stack=[]
    while temp!=None:
        stack.append(temp.val)
        temp=temp.next
    temp=head
    for _ in range(len(stack)):
        e=stack.pop()
        temp.val=e
        print(temp.val,end="->")
        temp=temp.next
    print("None")
#sc=o(n )
reverse(linkedlist.head)

#Reverse a linked list
def optimal_reverse(head):
    temp=head
    prev=None
    while temp!=None:
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev
ans=optimal_reverse(linkedlist.head)
print(ans.val)
temp=ans
while temp!=None:
    print(temp.val,end="->")
    temp=temp.next
print("None")

#Is Cycle present??
def ll_cycle(head):#o(n) sc=o(n)
    temp=head
    My_set=set()
    while temp!=None:
        if temp not in My_set:#We should not check for temp.val cause value may be multiple in various location but address should not be same is address is same there cycle exixst
            My_set.add(temp)
            temp=temp.next
        else:
            return True #Or return node
    return False
print(ll_cycle(linkedlist.head))#Brute
def optimal_ll_cycle(head):#o(n) sc=o(1)
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def ll_cycle2(head):#o(n) sc=o(1)
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
    return None #If intiution confusion watch video part-60 ll cycle part-2


#Find the lenght of the loop
def lenght(head):
    temp=head
    my_dict={}
    travel=0
    while temp!=None:
        if temp not in my_dict:
            my_dict[temp]=travel
            travel+=1
            temp=temp.next
        else:
            return travel-my_dict[temp]
    return None
ans=lenght(node1)
print(ans)

#Idea is when slow==fast occurs just move slow until it meets fast again and increase count value
def optimal_lenght(head):#tc=o(n) sc=o(1)
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            count=1
            slow=slow.next
            while slow!=fast:
                count+=1
                slow=slow.next
            return 
    return 0
ans=optimal_lenght(node1)
print(ans)  


#Change ll into frst even nodes and odd nodes
def odd_even(head):
    values=[]
    temp=head
    while temp:
        values.append(temp.val)
        if temp.next:
            temp=temp.next.next
        else:
            temp=None
    temp=head.next
    while temp:
        values.append(temp.val)
        if temp.next:
            temp=temp.next.next
        else:
            temp=None
    temp=head
    for i in range(len(values)):
        temp.val=values[i]
        print(temp.val,end='->')
        temp=temp.next
    print("None")
odd_even(linkedlist.head)

def op_odd_even(head):
    odd=head
    even=head.next
    even_head=even
    while even is not None and even.next is not None:
        odd.next=odd.next.next
        odd=odd.next
        even.next=even.next.next
        even=even.next
    odd.next=even_head
    temp=head
    while temp is not None:
        print(temp.val,end='->')
        temp=temp.next
    print("None")
op_odd_even(linkedlist.head)

#Remove the node from last
def remove_from_last(head,nth):
    count=0
    temp=head
    while temp:
        count+=1
        temp=temp.next
    if nth==count:
        head=head.next
        return head
    index_to_stop=count-nth
    prev=None
    temp=head
    n=0
    while n!=index_to_stop:
        prev=temp
        temp=temp.next
        n+=1
    prev.next=temp.next
    return head
remove_from_last(linkedlist.head,2)

def op_remove_from_last(head,nth):
    head_start=head
    norm_start=head
    n=0
    while n<nth:
        head_start=head_start.next
        n+=1
    if head_start==None:
        head=head.next
        return head
    prev=None
    while head_start is not None:
        head_start=head_start.next
        prev=norm_start
        norm_start=norm_start.next
    prev.next=norm_start.next
    return head
temp=op_remove_from_last(linkedlist.head,2)
while temp is not None:
    print(temp.val,end='->')
    temp=temp.next
print("None")
