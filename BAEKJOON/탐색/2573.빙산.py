def f(i,j):
    global island,visited,rear,front

    rear = (rear+1)%(M*N)
    q[rear] = [i,j]
    visited[i][j] = v
    while front != rear:
        front = (front+1)%(M*N)
        i,j = q[front]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] != v and arr[ni][nj] !=0:
                rear = (rear+1)%(M*N)
                q[rear] = [ni,nj]
                visited[ni][nj] = v
    island += 1
    rear = front = -1

di,dj = [0,1,0,-1],[1,0,-1,0]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

q = [0]*(N*M)
front = rear = -1
visited = [[0]*M for i in range(N)]
v = 1
time = 0
while 1:
    time += 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:

                # 좌표와 깍이는 수 입력
                cnt = 0
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                        cnt += 1
                rear = (rear+1)%(M*N)
                q[rear] = [i,j,cnt]

    for l in range(rear+1):
        i,j,cnt = q[l]
        arr[i][j] = max(0, arr[i][j]-cnt)
    rear = -1

    island = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j] != v:
                f(i,j)
    v += 1
    if island == 0:
        print(0)
        break
    if island > 1:
        print(time)
        break