import sys
sys.stdin = open('정사각형.txt', 'r')

def enQ(a):
    global rear, q
    rear = (rear+1)%4
    q[rear] = a

def deQ():
    global front, q
    front = (front+1)%4
    return q[front]

def f(i,j):
    global maxV, location, q, cnt

    enQ([i, j])
    v = rooms[i][j]

    while front != rear:
        i,j = deQ()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if rooms[ni][nj]-rooms[i][j] == 1:
                    if cnt[ni][nj] < cnt[i][j] + 1:
                        enQ([ni, nj])
                        cnt[ni][nj] = cnt[i][j] + 1

                        if cnt[ni][nj] > maxV:
                            maxV = cnt[ni][nj]
                            location = v
                        elif  cnt[ni][nj] == maxV:
                            if location > v:
                                location = v

di = [0,1,0,-1]
dj = [1,0,-1,0]
for t in range(int(input())):
    N = int(input())
    rear = front = -1
    q = [0] * 4

    rooms = [list(map(int, input().split())) for _ in range(N)]

    cnt = [[1] * N for _ in range(N)]

    maxV = 0
    location = float('INF')
    for i in range(N):
        for j in range(N):

            f(i,j)

    print('#{}'.format(t+1), end=' ')
    print(location,maxV)