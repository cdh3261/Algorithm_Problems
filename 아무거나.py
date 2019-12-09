import sys
sys.stdin = open('아무거나.txt', 'r')

def f(i, j):
    global visited, v, jud

    c = 1
    I, J = i, j
    point = arr[i][j]

    q = [[i, j]]
    visited[i][j] = v
    while q:
        qo = q.pop(0)
        i = qo[0]
        j = qo[1]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N:
                if nj == -1:
                    nj = M-1
                elif nj == M:
                    nj = 0

                if arr[ni][nj] == point and visited[ni][nj] != v:
                    visited[ni][nj] = v
                    jud = True
                    q.append([ni, nj])
                    arr[ni][nj] = 0
                    c += 1
    if c>1:
        arr[I][J] = 0


di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
case = [list(map(int, input().split())) for _ in range(T)]

visited = [[0]*M for _ in range(N)]
v = 1

for i in range(T):
    n, d, cnt = case[i]


    for nth in range(n, N+1, n):
        nth -= 1
        if d == 0:
            arr[nth] = arr[nth][cnt*(-1):]+arr[nth][:cnt*(-1)]
        else:
            arr[nth] = arr[nth][cnt:]+arr[nth][:cnt]

    jud = False
    for x in range(N):
        for y in range(M):
            if arr[x][y] != 0:
                f(x, y)
    v += 1
    total = N*M
    if jud == False:
        s = 0
        for x in range(N):
            for y in range(M):
                if arr[x][y] == 0:
                    total -= 1
                else:
                    s += arr[x][y]
        if total != 0:
            avg = s/total
            for x in range(N):
                for y in range(M):
                    if arr[x][y] != 0:
                        if arr[x][y]>avg:
                            arr[x][y] -= 1
                        elif arr[x][y]<avg:
                            arr[x][y] += 1
        else:
            break
ss = 0
for i in range(N):
    print(arr[i])
    for j in range(M):
        ss += arr[i][j]
print(ss)