def f(x,y,cnt,start):
    global maxV,visited,res

    if maxV < cnt:
        maxV = cnt
        res = [start]
    elif maxV == cnt:
        if res[-1] != start: #or not res:
            res.append(start)

    for j in range(N):
        if arr[x][j] == 1 and x != j and visited[x][j] != v:
            visited[x][j] = v
            f(j,x,cnt+1,start)


N,M = map(int,input().split())
arr = [[0]*N for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    arr[b-1][a-1] = 1

visited = [[0]*N for _ in range(N)]
v = 1
maxV = 0
res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            visited[i][j] = v
            f(j,i,1,i+1)
            v += 1
print(' '.join(map(str, res)))