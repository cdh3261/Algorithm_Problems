def walking(i,j,N,cnt,cut):
    global mount, visited, saveload, K
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    stack = []
    stack.append([i, j])
    visited[i][j] = 1

    while stack:
        qo = stack.pop()
        i = qo[0]
        j = qo[1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if nj >= 0 and ni >= 0 and ni < N and nj < N and mount[ni][nj] < mount[i][j] and visited[ni][nj] == 0:
                if mount[ni][nj]-mount[i][j] < cut:
                    mount[ni][nj] -= cut
                    first = mount[ni][nj]
                    second = mount[ni][nj]-cut
                    cut = 0
                    visited[ni][nj] = 1
                    cnt += 1
                    if cnt > saveload:
                        saveload = cnt
                    walking(ni, nj, N,cnt,cut)
                    visited[ni][nj] = 0
                    cnt -= 1
                    if first != second:
                        cut = K

for t in range(int(input())):
    N, K = map(int, input().split())
    cut = K
    mount = [list(map(int, input().split())) for i in range(N)]
    visited = [[0] * N for _ in range(N)]
    m = max(max(mount))
    cnt = 1
    saveload = 1
    for i in range(N):
        for j in range(N):
            if mount[i][j] == m:
                walking(i,j,N,cnt,cut)
    print('#{} {}'.format(t+1,saveload))
