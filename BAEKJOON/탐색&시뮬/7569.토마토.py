import sys
input = sys.stdin.readline

d = [[0,1,0],[1,0,0],[0,-1,0],[-1,0,0],[0,0,1],[0,0,-1]]

M,N,H = map(int,input().split())
arr = [[list(map(int,input().split())) for i in range(N)] for j in range(H)]
visited = [[[0]*M for i in range(N)] for j in range(H)]

cnt = N*M*H
q = [0]*(N*M*H)
r = f = -1
for z in range(H):
    for i in range(N):
        for j in range(M):
            if arr[z][i][j] == -1:
                cnt -= 1
            elif arr[z][i][j] == 1:
                r += 1
                q[r] = [z,i,j]

day = 0
while f != r:
    f += 1
    z,i,j = q[f]
    cnt -= 1
    for a,b,c in d:
        nz,ni,nj = z+c,i+a,j+b
        if 0<=nz<H and 0<=ni<N and 0<=nj<M and visited[nz][ni][nj]==0 and arr[nz][ni][nj]==0:
            day = visited[nz][ni][nj] = visited[z][i][j] + 1
            r += 1
            q[r] = [nz,ni,nj]

if cnt == 0:
    print(day)
else:
    print(-1)