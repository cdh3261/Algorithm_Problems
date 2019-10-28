def bfs():
    global q, distance, front, rear, tomato, N, M

    cnt = 0
    maxV = 0
    while rear != front:
        front += 1
        i,j = q[front]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and distance[ni][nj] == -1 and arr[ni][nj] == 0:
                rear += 1
                q[rear] = [ni, nj]
                distance[ni][nj] = distance[i][j] + 1
                cnt += 1
                if maxV < distance[ni][nj]:
                    maxV = distance[ni][nj]
    if tomato != cnt:
        return -1
    else:
        return maxV

di = [1,0,-1,0]
dj = [0,1,0,-1]

M,N = map(int, input().split())
arr =  [list(map(int, input().split())) for i in range(N)]

distance = [[-1]*M for i in range(N)]
rear = front = -1
q = [0]*N*M
tomato = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            distance[i][j] += 1
            rear += 1
            q[rear] = [i, j]
        elif arr[i][j] == 0:
            tomato += 1

if q:
    print(bfs())
else:
    print(0)