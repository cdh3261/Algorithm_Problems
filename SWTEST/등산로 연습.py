import sys
sys.stdin = open('mount.txt', 'r')

def walking(i,j,N,cnt):
    global mount, visited, saveload
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
                visited[ni][nj] = 1
                cnt += 1
                if cnt > saveload:
                    saveload = cnt
                walking(ni, nj, N,cnt)
                visited[ni][nj] = 0
                cnt -= 1

for t in range(int(input())):
    N, K = map(int, input().split())

    mountt = [list(map(int, input().split())) for i in range(N)]
    visited = [[0] * N for _ in range(N)]

    saveload = 1

    for w in range(K+1):
        for i in range(N):
            for j in range(N):
                mount = mountt[:]
                mount[i][j] -= w
                m = 0
                for g in range(N):
                    for h in range(N):
                        if mount[g][h] > m:
                            m = mount[g][h]
                for e in range(N):
                    for r in range(N):
                        cnt = 1
                        if mount[e][r] == m:
                            walking(e,r,N,cnt)
    print(saveload)
