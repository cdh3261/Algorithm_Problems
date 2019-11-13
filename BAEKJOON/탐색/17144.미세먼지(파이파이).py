def enQ(a):
    global rear, q
    rear = (rear+1)%(N*M)
    q[rear] = a

def deQ():
    global front, q
    front = (front+1) % (N*M)
    return q[front]

def f(i,j,k,A,B,d):
    while 1:
        ni = i + di[k]
        nj = j + dj[k]
        if d == 1:
            if A<ni<B and 0<=nj<M:
                if arr[ni][nj] == -1:
                    return
                if arr[ni][nj] != 0:
                    if arr[i][j] == -1:
                        arr[ni][nj] = 0
                    else:
                        arr[i][j],arr[ni][nj] = arr[ni][nj],0
                i,j = ni,nj
            elif ni == A:
                k = 1
            elif nj == M:
                k = 2
            elif ni == B:
                k = 3
            elif nj == -1:
                k = 0
        else:
            if A<ni<B and 0<=nj<M:
                if arr[ni][nj] == -1:
                    return
                if arr[ni][nj] != 0:
                    if arr[i][j] == -1:
                        arr[ni][nj] = 0
                    else:
                        arr[i][j],arr[ni][nj] = arr[ni][nj],0
                i,j = ni,nj
            elif ni == A:
                k = 3
            elif nj == M:
                k = 0
            elif ni == B:
                k = 1
            elif nj == -1:
                k = 2


# 상, 우, 하, 좌
di,dj = [-1,0,1,0],[0,1,0,-1]
N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

robot = [[i,0,0] for i in range(N) if arr[i][0] == -1]
robot[1][2] = 2
front = rear = -1
q = [0]*(N*M)
for time in range(T):

    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 5:
                enQ([i,j,arr[i][j]//5])
    while front != rear:
        qo = deQ()
        i,j,x = qo[0],qo[1],qo[2]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] != -1:
                arr[ni][nj] += x
                arr[i][j] -= x

    f(robot[0][0],robot[0][1],robot[0][2],-1,robot[1][0],1)
    f(robot[1][0],robot[1][1],robot[1][2],robot[0][0],N,2)

s = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] >=0:
            s += arr[i][j]
print(s)