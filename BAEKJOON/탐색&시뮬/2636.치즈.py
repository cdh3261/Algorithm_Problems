def hole(i,j):
    global visited
    jud = True
    visited[i][j] = 1
    q = [[i,j]]
    r = [[i,j]]
    while q:
        i,j = q.pop(0)
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                if ni == 0 or ni == N or nj == 0 or nj == M:
                    jud = False
                q.append([ni,nj])
                r.append([ni,nj])
                visited[ni][nj] = 1

    if jud:
        while r:
            i,j = r.pop()
            arr[i][j] = 2



di,dj = [0,1,0,-1],[1,0,-1,0]
N,M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
res = []
time = 0
while 1:
    visited = [[0]*M for _ in range(N)]

    cnt = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if (arr[i][j] == 0 or arr[i][j] == 2) and visited[i][j] == 0:
                hole(i,j)

    q = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1

                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                        q.append([i,j])

                        break
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                arr[i][j] = 0
    res.append(cnt)
    for i,j in q:
        arr[i][j] = 0
        cnt -= 1

    if cnt == 0:
        break

    time += 1

print(time+1)
print(res[-1])