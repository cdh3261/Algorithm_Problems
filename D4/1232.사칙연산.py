import sys
sys.stdin = open('사칙연산.txt', 'r')

def enQueue(n):
    global rear, q
    rear += 1
    q[rear] = n

def deQueue(n):
    global front, q
    front += 1
    return q[front]

def inorder(n):
    global ch1, ch2, q, tree

    if ch1[n]:
        inorder(ch1[n])
        enQueue(tree[ch1[n]])
    if ch2[n]:
        inorder(ch2[n])
        enQueue(tree[ch2[n]])


def calculate(N):
    global q

    operand = []
    for i in range(N):
        n = deQueue(i)
        if n == '+':
            num2 = operand.pop(-1)
            num1 = operand.pop(-1)
            operand.append((num1 + num2))
        elif n == '-':
            num2 = operand.pop(-1)
            num1 = operand.pop(-1)
            operand.append((num1 - num2))
        elif n == '*':
            num2 = operand.pop(-1)
            num1 = operand.pop(-1)
            operand.append((num1 * num2))
        elif n == '/':
            num2 = operand.pop(-1)
            num1 = operand.pop(-1)
            operand.append((num1 / num2))
        else: # 숫자
            operand.append(n)
    return int(operand[-1])

TC = 10
for t in range(TC):
    N = int(input())
    rear = front = -1
    q = [0]*N

    tree = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)

    for i in range(1,N+1):
        cal = list(input().split())
        if len(cal) == 4:
            tree[i] = cal[1]
            ch1[i] = int(cal[2])
            ch2[i] = int(cal[3])
        else:
            tree[i] = int(cal[1])

    inorder(1)
    q[-1] = tree[1]

    print('#{} {}'.format(t+1, calculate(N)))