def enQueue(a):
    global rear, computers
    rear += 1
    computers[rear] = a

def deQueue():
    global front, computers
    front += 1
    return computers[front]

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    if joint[b]> joint[a]:
        p[a] = b
    else:
        p[b] = a
        if joint[a] == joint[b]:
            joint[a] += 1

# 컴퓨터 수
N = int(input())
# 연결 선의 수
M = int(input())
computers = [list(map(int, input().split())) for i in range(M)]
computers.sort(key=lambda x: x[2])

p = [i for i in range(N+1)]
joint = [0]*(N+1)

rear = front = -1

cnt = 0
minV = 0
while cnt < N-1:
    x, y, d = deQueue()
    dx, dy = find(x), find(y)
    if dx != dy:
        union(dx, dy)
        cnt += 1
        minV += d

print(minV)