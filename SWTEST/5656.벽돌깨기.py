import sys,time
sys.stdin = open('벽돌깨기.txt', 'r')

def enQ(a):
    global rear, q
    rear = (rear+1)%(W*H)
    q[rear] = a

def deQ():
    global front, q
    front = (front+1)%(W*H)
    return q[front]


def npr(n,k):
    global p, Nth
    if n == k:
        Nth.append(p[:])
    else:
        for m in range(W):
            p[n]=m
            npr(n+1,k)

def f(i,j):
    global q,rear,front

    enQ([i,j])
    while rear != front:
        i,j = deQ()
        v=mir[i][j]
        mir[i][j] = 0
        for k in range(4):
            ni,nj = i,j
            if k == 0:
                for z in range(v-1):
                    ni += di[k]
                    nj += dj[k]
                    if 0<=ni<H and 0<=nj<W and mir[ni][nj] != 0:
                        if mir[ni][nj]>1:
                            enQ([ni,nj])
                        elif mir[ni][nj] == 1:
                            mir[ni][nj] = 0
            elif k == 1:
                for z in range(v-1):
                    ni += di[k]
                    nj += dj[k]
                    if 0<=ni<H and 0<=nj<W and mir[ni][nj] != 0:
                        if mir[ni][nj]>1:
                            enQ([ni,nj])
                        elif mir[ni][nj] == 1:
                            mir[ni][nj] = 0
            elif k == 2:
                for z in range(v-1):
                    ni += di[k]
                    nj += dj[k]
                    if 0<=ni<H and 0<=nj<W and mir[ni][nj] != 0:
                        if mir[ni][nj]>1:
                            enQ([ni,nj])
                        elif mir[ni][nj] == 1:
                            mir[ni][nj] = 0
            else:
                for z in range(v-1):
                    ni += di[k]
                    nj += dj[k]
                    if 0 <= ni < H and 0 <= nj < W and mir[ni][nj] != 0:
                        if mir[ni][nj] > 1:
                            enQ([ni, nj])
                        elif mir[ni][nj] == 1:
                            mir[ni][nj] = 0


di = [0,1,0,-1]
dj = [1,0,-1,0]
for t in range(int(input())):
    start_time = time.time()
    N,W,H = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]

    rear = front = -1
    q = [0] * W * H

    Nth = []
    p = [0]*N
    npr(0,N)
    minV = float('INF')
    for i in range(len(Nth)):

        mir = [[0] * W for _ in range(H)]
        for j in range(H):
            for k in range(W):
                mir[j][k] = arr[j][k]
        V = W*H
        for j in range(N):
            for k in range(H):
                if mir[k][Nth[i][j]] != 0:
                    I,J = k,Nth[i][j]
                    f(I,J)
                    break

            for a in range(W):
                for b in range(H):
                    if mir[-b-1][a]==0:
                        zero = -b-1
                        idx = -b-1
                        while 1:
                            if idx < -H:
                                break
                            if mir[idx][a] == 0:
                                idx -= 1
                            else:
                                mir[idx][a],mir[zero][a] = mir[zero][a],mir[idx][a]
                                break
        for _ in range(H):
            V -= mir[_].count(0)
        minV = min(minV, V)
        if minV == 0:
            break
    print('#{} {}'.format(t+1,minV))
    print('%.4fsec' %(time.time()-start_time))