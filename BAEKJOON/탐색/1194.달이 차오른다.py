def dfs(i,j):
    global visited, v, find_keys, cnt,minV
    if minV <= cnt:
        return


    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M and visited[ni][nj] != v:
            if arr[ni][nj] == '.':
                cnt += 1
                visited[ni][nj] = v
                dfs(ni,nj)
                cnt -= 1
                # v += 1
                visited[ni][nj] = v-1
                # visited[i][j] = 0

            elif arr[ni][nj] in keys:
                cnt += 1
                find_keys.append(arr[ni][nj].upper())
                v += 1
                visited[ni][nj] = v
                dfs(ni,nj)
                cnt -= 1
                find_keys.pop()
                visited[ni][nj] = v-1
                # visited[i][j] = 0

            elif arr[ni][nj] == '#':
                # v += 1
                pass
            #문을 발견했을 때, 그 문을 열수 있는 열쇠가 있으면
            elif arr[ni][nj] in doors:
                if arr[ni][nj] in find_keys:
                    cnt += 1
                    # stack.append([ni,nj])
                    visited[ni][nj] = v
                    dfs(ni,nj)
                    cnt -= 1
                    # v += 1
                    visited[ni][nj] = v-1
                    # visited[i][j] = 0
                # else:
                #     visited[i][j] = 0

                # v += 1
            elif arr[ni][nj] == '1':
                cnt += 1
                minV = min(minV, cnt)
                # return 1
    # visited[i][j] = 0



keys = ['a','b','c','d','e','f']
doors = ['A','B','C','D','E','F']
di,dj = [0,1,0,-1],[1,0,-1,0]
# .복도 #벽 a-f열쇠 A-F문 0현재위치 1출구
N,M = map(int,input().split())
arr = [list(input()) for i in range(N)]

minV = float('INF')
find_keys = []
v = 1
cnt = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            arr[i][j] = '.'
            visited[i][j] = v
            dfs(i,j)
            if cnt == 0:
                print(-1)
            else:
                print(minV)
            break