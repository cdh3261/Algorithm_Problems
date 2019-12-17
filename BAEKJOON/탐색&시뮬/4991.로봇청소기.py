def npr(n,k,s):
    global minV

    if s >= minV:
        return

    if n == k:
        if minV > s:
            minV = s
        return

    for m in range(1,C):
        if used[m] == 0:
            used[m] = 1
            p[n] = m+1
            npr(n+1,k,s+points[p[n-1]-1][p[n]-1])
            used[m] = 0

def bfs(i,j,start):
    global  C
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    q = [[i,j]]
    while q:
        qo = q.pop(0)
        i,j = qo[0],qo[1]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] != 'x':
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni,nj])
                if arr[ni][nj] != '.' and arr[ni][nj] != 'x':
                    # 시작 노드 번호, *의 노드번호, 거리
                    points[start-1][arr[ni][nj]-1] = visited[ni][nj]-1
                    points[arr[ni][nj]-1][start-1] = visited[ni][nj]-1

di,dj = [0,1,0,-1],[1,0,-1,0]
while 1:
    M,N = map(int,input().split())
    if N == 0 and M == 0:
        break
    # . 깨끗한칸 * 더러운칸 x 가구 o시작위치
    arr = [list(input()) for _ in range(N)]

    C = 0 # 노드 개수
    V = 2 # 각각의 번호
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'o':
                arr[i][j] = 1
                C += 1
            elif arr[i][j] == '*':
                arr[i][j] = V
                V += 1
                C += 1

    points = [[0]*C for i in range(C)]

    a = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '.' and arr[i][j] != 'x':
                bfs(i,j,arr[i][j])
                a += 1
        if a == C+1:
            break

    minV = 10000000
    for i in range(1,C):
        if points[i-1][i] == 0:
            minV = -1
            break

    if minV != -1:
        used = [0]*C
        p = [1]*C
        npr(1,C,0)
    print(minV)