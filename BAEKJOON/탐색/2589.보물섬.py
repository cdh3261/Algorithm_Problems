def f(i,j):
    global maxV
    visited = [[0]*M for _ in range(N)]
    q = [[i,j]]
    visited[i][j] = 1
    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and arr[ni][nj]=='L':
                visited[ni][nj] = visited[i][j]+1
                q.append([ni,nj])
                if visited[ni][nj]>maxV:
                    maxV = visited[ni][nj]

di,dj = [0,1,0,-1],[1,0,-1,0]
N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

maxV = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            f(i,j)

print(maxV-1)