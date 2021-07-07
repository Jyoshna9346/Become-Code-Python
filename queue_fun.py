def enqueue(val):
    global size
    global front
    global rear
    global queue
    if rear==size-1:
        print("Queue is Full")
    else:
        queue.append(val)
        rear+=1
        if front==-1:
            front=0
    
def dequeue():
    global size
    global front
    global rear
    global queue
    if front==-1:
        return "Queue is empty"
    else:
        if(rear==0):
            front=-1
        rear-=1
        val=queue.pop(0)
        return val
        
def display():
    global size
    global front
    global rear
    global queue
    if front==-1:
        print("Queue is empty")
    else:
        for i in range(front,rear+1):
            print(queue[i],end=" ")
    

size=int(input("Enter Size"))
front=-1
rear=-1
queue=[]
while(True):
    ch=int(input("1.enqueue 2. dequeue 3.display 4.exit"))
    if ch==1:
        val=int(input())
        enqueue(val)
    elif ch==2:
        print(dequeue())
    elif ch==3:
        display()
    else:
        break
