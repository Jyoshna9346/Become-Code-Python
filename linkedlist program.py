'''Linked list:'''

#creating a node:
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
NN1=Node(10)
NN2=Node(100)
NN3=Node(200)
NN1.next=NN2
NN2=next=NN3
'''
'''    
>>> NN
<__main__.Node object at 0x000001087535EEB0>
>>> NN.data
10
>>> NN.next
>>> print(NN.next)
None
'''
head=None
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_end(NN):
    global head
    if head==None:
        head=NN
    else:
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=NN
def display(head):
    if head==None:
        print("No Nodes")
    else:
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
while True:
    ch=int(input("1.insert at end 7.display. 8.exit"))
    if ch==1:
        data=int(input())
        NN=Node(data) #node creation
        insert_at_end(NN)
    elif ch==7:
        display(head)
    else:
        break 
