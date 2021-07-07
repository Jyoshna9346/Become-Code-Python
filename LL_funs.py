class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


def insert_end(val):
    global head
    global tail
    NN=Node(val)# creating New Node
    if head==None and tail==None:
        head=NN
        tail=NN
    else:
        tail.next=NN
        tail=NN
def insert_front(val):
    global head
    global tail
    NN=Node(val)# creating New Node
    if head==None and tail==None:
        head=NN
        tail=NN
    else:
        NN.next=head
        head=NN
                
def insert_pos(val,pos):
    global head
    global tail
    NN=Node(val)# creating New Node
    if head==None and tail==None:
        head=NN
        tail=NN
    else:
        temp=head# 10 20 30 40 50        100
        while pos-2:
            temp=temp.next
            pos-=1
        NN.next=temp.next
        temp.next=NN
        
def display():
    global head
    if head==None:
        print("No Nodes")
    else:
        temp=head
        while temp:
            print(temp.val)
            temp=temp.next
def delete_end():
    global head
    global tail
    if head==None:
        return "No Nodes to delete"
    if head==tail:
        val=head.val
        head=None
        tail=None
        return val
    temp=head
    while(temp.next.next):
        temp=temp.next
    val=temp.next.val
    temp.next=None
    tail=temp
    return val
        
def delete_front():
    global head
    global tail
    if head==None:
        return "No Nodes to delete"
    if head==tail:
        val=head.val
        head=None
        tail=None
        return val
    temp=head
    head=head.next
    temp.next=None
    return temp.val
def delete_pos(pos):
    global head
    global tail
    if head==None:
        return "No Nodes to delete"
    if head==tail:
        val=head.val
        head=None
        tail=None
        return val
    temp=head
    i=1
    while(i<pos-1):
        temp=temp.next
        i+=1
    val=temp.next.val
    temp.next=temp.next.next
    return val
    
    
head=None
tail=None
while(True):
    ch=int(input("""1.Insert at end 2.Insert at front 3.Insert by pos
            
        4.display 5.delete at end 6. delete at head 7. delete by pos 10.exit"""))
    
    if ch==1:
        val=int(input())
        insert_end(val)
    elif ch==2:
        val=int(input())
        insert_front(val)
    elif ch==3:
        val=int(input())
        pos=int(input())
        insert_pos(val,pos)
    elif ch==4:
        display()
    elif ch==5:
        print(delete_end())
    elif ch==6:
        print(delete_front())
    elif ch==7:
        pos=int(input())
        print(delete_pos(pos))
    else:
        break
        
