def f(i,j):
    global visited,v,jud
    cnt = 1
    same = [[i,j]]
    s = arr[i][j]
    q = [[i,j]]
    visited[i][j] = v
    while q:
        i,j = q.pop(0)
        for x,y in [0,1],[1,0],[0,-1],[-1,0]:
            ni,nj = i+x,j+y
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] != v and L<=abs(arr[i][j]-arr[ni][nj])<=R:
                visited[ni][nj] = v
                cnt += 1
                q.append([ni,nj])
                same.append([ni,nj])
                s += arr[ni][nj]
    if cnt == 1:
        jud = False
        return

    jud = True
    avg = s//cnt
    for i in range(cnt):
        arr[same[i][0]][same[i][1]] = avg


N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

jud = True
visited = [[0]*N for _ in range(N)]
v = 1

total = 0
pre = 0
res = 0
while 1:
    for i in range(N):
        for j in range(N):
            if visited[i][j] != v:
                f(i,j)
                if jud == True:
                    res = 1
                    # total += 1
                    # print('ARR')
                    # for z in range(N):
                    #     print(arr[z])
    if res:
        total += 1


    if pre == total:
        break
    res = 0
    pre = total
    v += 1

print(total)