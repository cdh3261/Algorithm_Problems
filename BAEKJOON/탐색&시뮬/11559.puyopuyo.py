def f(i,j):
    global visited,remove,total,jud

    cnt = 1
    start = arr[i][j]
    q = [[i,j]]
    save = [[i,j]]
    while q:
        i,j = q.pop(0)
        for x,y in (1,0),(-1,0),(0,1),(0,-1):
            ni,nj = i+x,j+y
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] != v and arr[ni][nj] == start:
                visited[ni][nj] = v
                q.append([ni,nj])
                save.append([ni,nj])
                cnt += 1

    if cnt >= 4:
        jud = True
        remove.append(save)
        total += 1

N,M = 12,6
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
v = 1
# 밑에서부터 봄.
# 몇 연쇄가 일어나는지 판단.
# 여러 그룹이 동시에 터지면 한번의 연쇄가 추가.
result = 0
while 1:
    jud = False
    remove = []
    total = 0
    for i in range(N-1,-1,-1):
        for j in range(M):
            if visited[i][j] != v and arr[i][j] != '.':
                visited[i][j] = v
                f(i,j)

    if total > 1 or jud:
        result += 1
    elif jud == False:
        break

    for i in range(total):
        for x,y in remove[i]:
            arr[x][y] = '.'

    for j in range(M):
        for i in range(N-1,-1,-1):
            if arr[i][j] == '.':
                k = i-1
                while k != -1:
                    if arr[k][j] != '.':
                        arr[i][j],arr[k][j] = arr[k][j],'.'
                        break
                    k -= 1
                if k == -1:
                    break
    v += 1

print(result)