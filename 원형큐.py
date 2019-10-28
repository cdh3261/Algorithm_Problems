def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue is Full")
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue is Empty")
    else:
        front = (front+1) % len(cQ)
        return cQ[front]


cQ_size = 4
cQ = [0] * cQ_size
front = rear = 0