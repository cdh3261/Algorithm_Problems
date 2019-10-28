def dfs(i,j,n,z):
    global cnt

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    q = []
    q.append([i, j])
    while q:
        po = q.pop(0)
        i, j = po[0], po[1]
        safe[i][j] = 0

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < n and nj >= 0 and nj < n:
                if safe[ni][nj] > z:
                    q.append([ni, nj])
    cnt += 1
    return 1

tc = int(input())
safe = []
for t in range(tc):
    safe.append(list(map(int, input().split())))

sm = safe[0][0]
la = safe[0][0]
for i in range(tc):
    for j in range(tc):
        s = safe[i][j]
        if s < sm:
            sm = s
        if s > la:
            la = s

res = []
for z in range(sm, la):
    cnt = 0
    for i in range(tc):
        for j in range(tc):
            if safe[i][j] > z:
                dfs(i,j,tc,z)
    res.append(cnt)
print(max(res))