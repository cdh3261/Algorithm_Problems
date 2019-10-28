import sys
input = sys.stdin.readline

def check(i, j, c):
    global arr, N, minV, visit, M

    q = []
    q.append([i,j])
    while q:
        qo = q.pop(0)
        i = qo[0]
        j = qo[1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            w,z = ni,nj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                # 위로 갈때
                if k == 0:
                    for a,b in (-1,-1), (-1,1):
                        jud = 0
                        ni = w
                        nj = z
                        # 대각선이동
                        for l in range(2):
                            ni += a
                            nj += b
                            if 0<=ni<N and 0<=nj<M:
                                if jud == 0:
                                    if arr[ni][nj] == 'King':
                                        break

                                elif jud == 1:
                                    if not (arr[ni][nj] == 'King' or visit[ni][nj]==1):
                                        break
                                    elif arr[ni][nj] == 'King':
                                        return visit[i][j]

                                jud += 1

                        if jud == 2:
                            q.append([ni, nj])
                            visit[ni][nj] = visit[i][j]+1

                # 아래로 갈때
                elif k == 1:
                    for a,b in (1,-1), (1,1):
                        jud = 0
                        ni = w
                        nj = z
                        #대각선 이동
                        for l in range(2):
                            ni += a
                            nj += b
                            if 0<=ni<N and 0<=nj<M:
                                if jud == 0:
                                    if arr[ni][nj] == 'King':
                                        break

                                elif jud == 1:
                                    if not (arr[ni][nj] == 'King' or visit[ni][nj] == 1):
                                        break
                                    elif arr[ni][nj] == 'King':
                                        return visit[i][j]

                                jud += 1

                            if jud == 2:
                                q.append([ni, nj])
                                visit[ni][nj] = visit[i][j] + 1
                elif k == 2:
                    for a,b in (-1,-1), (1,-1):
                        jud = 0
                        ni = w
                        nj = z
                        for l in range(2):
                            ni += a
                            nj += b
                            if 0<=ni<N and 0<=nj<M:
                                if jud == 0:
                                    if arr[ni][nj] == 'King':
                                        break

                                elif jud == 1:
                                    if not (arr[ni][nj] == 'King' or visit[ni][nj] == 1):
                                        break
                                    elif arr[ni][nj] == 'King':
                                        return visit[i][j]

                                jud += 1

                            if jud == 2:
                                q.append([ni, nj])
                                visit[ni][nj] = visit[i][j] + 1
                else:
                    for a,b in (-1,1), (1,1):
                        jud = 0
                        ni = w
                        nj = z
                        for l in range(2):
                            ni += a
                            nj += b
                            if 0<=ni<N and 0<=nj<M:
                                if jud == 0:
                                    if arr[ni][nj] == 'King':
                                        break

                                elif jud == 1:
                                    if not (arr[ni][nj] == 'King' or visit[ni][nj] == 1):
                                        break
                                    elif arr[ni][nj] == 'King':
                                        return visit[i][j]

                                jud += 1

                            if jud == 2:
                                q.append([ni, nj])
                                visit[ni][nj] = visit[i][j] + 1
    return -1


di=[-1,1,0,0]
dj=[0,0,-1,1]

Sang_x, Sang_y = map(int, input().split())
x, y = map(int, input().split())
N = 10
M = 9

arr = [[0]*M for i in range(N)]
visit = [[1]*M for i in range(N)]
arr[x][y] = 'King'
minV = N*N

print(check(Sang_x,Sang_y, 0))