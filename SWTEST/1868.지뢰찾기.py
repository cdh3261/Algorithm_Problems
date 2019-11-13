import sys
sys.stdin = open('지뢰찾기.txt', 'r')


def f(i, j):
    global visited

    visited[i][j] = 1
    q = []
    q.append([i, j])
    while q:
        qo = q.pop(0)
        i = qo[0]
        j = qo[1]
        for k in range(8):
            ni = i+di[k]
            nj = j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1


def e(i, j):
    global cnt

    for k in range(8):
        ni = i+di[k]
        nj = j+dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                return
    cnt += 1


di, dj = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
for t in range(int(input())):
    N = int(input())
    arr = [list(input()) for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                jud = True
                for k in range(8):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '*':
                        arr[i][j] = 1
                        jud = False
                        break
                if jud:
                    arr[i][j] = 0

    visited = [[0]*N for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and visited[i][j] == 0:
                cnt += 1
                f(i, j)
            elif arr[i][j] != '*' and visited[i][j] == 0:
                e(i, j)

    print('#{} {}'.format(t+1, cnt))