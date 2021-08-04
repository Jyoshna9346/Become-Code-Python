head=None#global 
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


def insert_at_head(NN):
    global head
    if head==None:
        head=NN
    else:
        NN.next=head
        head=NN

def insert_at_pos(NN,pos):
    global head
    if pos==1:
        insert_at_head(NN)
    elif head==None:
        head=NN
    else:
        temp=head
        p=1
        while p<pos-1:
            if temp.next==None:
                #print("List contains less count")
                break
            temp=temp.next
            p+=1
         
        #print(temp.data)
        NN.next=temp.next
        temp.next=NN
             
def delete_at_end():
    global head
    if head==None:
        print("No Nodes")
    else:
        temp=head
        if head.next==None:
            head=None
            return
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        

def display(head):
    if head==None:
        print("No Nodes")
    else:
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
while True:
    ch=int(input("1.Insert at end 2.Insert at Head 3.Insert by pos 4.delete at end 7.display, 8.exit"))
    if ch==1:
        data=int(input())
        NN=Node(data)# node creation
        insert_at_end(NN)
    elif ch==2:
        data=int(input())
        NN=Node(data)# node creation
        insert_at_head(NN)
    elif ch==3:
        data=int(input())
        pos=int(input())
        NN=Node(data)# node creation
        insert_at_pos(NN,pos)
    elif ch==4:
        delete_at_end()
        
    elif ch==7:
        display(head)
    else:
        break
