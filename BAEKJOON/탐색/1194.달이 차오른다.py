def d(i, j, k):
    q = [[i, j, k]]
    while q:
        qo = q.pop(0)
        i, j, k = qo[0], qo[1], qo[2]
        for m in range(4):
            ni = i+di[m]
            nj = j+dj[m]
            nk = k
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '1':
                    print(visited[i][j][k]+1)
                    return

                if arr[ni][nj] in doors and nk & (1<<(ord(arr[ni][nj])-ord('A'))) == 0:
                    continue

                elif arr[ni][nj] in keys:
                    nk |= (1 << (ord(arr[ni][nj])-ord('a')))

                # 방문한 곳이 아니고 벽이 아니면
                if visited[ni][nj][nk] == 0 and arr[ni][nj] != '#':
                    q.append([ni,nj,nk])
                    visited[ni][nj][nk] = visited[i][j][k]+1
    print(-1)

def f():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                arr[i][j] = '.'
                return d(i, j, 0)

keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(input()) for i in range(N)]
visited = [[[0]*64 for _ in range(M)] for _ in range(N)]
f()