def escape(i,j,N,M,L):
    global prison, arr

    q = []
    q.append([i, j])
    arr[i][j] = 1
    while q:
        qo = q.pop(0)
        i = qo[0]
        j = qo[1]

        if arr[i][j] < L:
            if prison[i][j] == 1:
                prison[i][j] = 0
                for k in range(4):
                    ni = i + di1[k]
                    nj = j + dj1[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and prison[ni][nj] != 4 and prison[ni][nj] != 7 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    elif k == 1:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and \
                                prison[ni][nj] != 6 and prison[ni][nj] != 5 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    elif k == 2:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and prison[ni][nj] != 6 and prison[ni][nj] != 7 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    elif k == 3:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and prison[ni][nj] != 4 and prison[ni][nj] != 5 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
            elif prison[i][j] == 2:
                prison[i][j] = 0
                for k in range(2):
                    ni = i + di2[k]
                    nj = j + dj2[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and prison[ni][nj] != 4 and prison[ni][nj] != 7 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    else:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and prison[ni][nj] != 5 and prison[ni][nj] != 6 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
            elif prison[i][j] == 3:
                prison[i][j] = 0
                for k in range(2):
                    ni = i + di3[k]
                    nj = j + dj3[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and \
                                prison[ni][nj] != 6 and prison[ni][nj] != 7 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    else:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and \
                                prison[ni][nj] != 4 and prison[ni][nj] != 5 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
            elif prison[i][j] == 4:
                prison[i][j] = 0
                for k in range(2):
                    ni = i + di4[k]
                    nj = j + dj4[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and \
                                prison[ni][nj] != 4 and prison[ni][nj] != 7 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    else:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and \
                                prison[ni][nj] != 5 and prison[ni][nj] != 4 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
            elif prison[i][j] == 5:
                prison[i][j] = 0
                for k in range(2):
                    ni = i + di5[k]
                    nj = j + dj5[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and \
                                prison[ni][nj] != 4 and prison[ni][nj] != 5 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    else:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and \
                                prison[ni][nj] != 5 and prison[ni][nj] != 6 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
            elif prison[i][j] == 6:
                prison[i][j] = 0
                for k in range(2):
                    ni = i + di6[k]
                    nj = j + dj6[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and \
                                prison[ni][nj] != 6 and prison[ni][nj] != 7 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    else:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and \
                                prison[ni][nj] != 5 and prison[ni][nj] != 6 and arr[ni][nj] == 0:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
            elif prison[i][j] == 7:
                prison[i][j] = 0
                for k in range(2):
                    ni = i + di7[k]
                    nj = j + dj7[k]
                    if k == 0:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 3 and \
                                prison[ni][nj] != 4 and prison[ni][nj] != 7:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
                    else:
                        if ni >= 0 and nj >= 0 and ni < N and nj < M and prison[ni][nj] != 0 and prison[ni][nj] != 2 and \
                                prison[ni][nj] != 7 and prison[ni][nj] != 6:
                            q.append([ni, nj])
                            arr[ni][nj] = arr[i][j] + 1
    cnt = 0
    for b in range(N):
        for c in range(M):
            if arr[b][c] != 0:
                cnt += 1
    return cnt

di1 = [-1,1,0,0]
dj1 = [0,0,-1,1]

di2 = [-1,1]
dj2 = [0,0]

di3 = [0,0]
dj3 = [-1,1]

di4 = [-1,0]
dj4 = [0,1]

di5 = [0,1]
dj5 = [1,0]

di6 = [0,1]
dj6 = [-1,0]

di7 = [-1,0]
dj7 = [0,-1]
TC = int(input())
for t in range(TC):
    N,M,Rx,Ry,L = map(int, input().split())
    prison = [list(map(int, input().split())) for i in range(N)]
    arr = [[0]*M for _ in range(N)]
    if L == 1:
        print('#{} 1'.format(t+1))
    else:
        print('#{} {}'.format(t+1, escape(Rx,Ry,N,M,L)))