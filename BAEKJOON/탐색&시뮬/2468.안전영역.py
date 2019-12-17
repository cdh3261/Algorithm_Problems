def bfs(i, j, n):
    global front,rear,q

    rear = (rear+1)%(tc*tc)
    q[rear] = [i, j]
    while front != rear:
        front = (front+1)%(tc*tc)
        i, j = q[front]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if ni>=0 and ni<n and nj>=0 and nj<n and visited[ni][nj] != v:
                visited[ni][nj] = v
                rear = (rear+1)%(tc*tc)
                q[rear] = [ni, nj]


di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
tc = int(input())
safe = [list(map(int, input().split())) for t in range(tc)]
la = max(max(safe))
res,v = 0,1

q = [0]*(tc*tc)
front = rear = -1

visited = [[0]*tc for i in range(tc)]
for z in range(la):
    cnt = 0
    for i in range(tc):
        for j in range(tc):
            if safe[i][j]<=z:
                visited[i][j] = v  # 침수영역 표시

    for i in range(tc):
        for j in range(tc):
            if visited[i][j] != v:
                bfs(i, j, tc)
                cnt += 1
    if cnt>res:
        res = cnt
    v += 1
print(res)