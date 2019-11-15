def find(a):
    while p[a] != a:
        a = p[p[a]]
    return p[a]

def union(a,b):
    if disjoint[b] > disjoint[a]:
        p[a] = p[b]
    else:
        p[b] = p[a]
        if disjoint[a] == disjoint[b]:
            disjoint[b] += 1



def up(i,j,node):
    global u,E

    ni=i-1
    nj=j
    if 0<=ni<N and 0<=nj<M and visited[ni][nj] != v and arr[ni][nj] != node:
        if arr[ni][nj]==0:
            u += 1
            up(ni,nj,node)
        else:
            if u>1 and node < arr[ni][nj] and not [node, arr[ni][nj], u] in res:
                E += 1
                res.append([node, arr[ni][nj], u])
            return

def down(i, j, node):
    global d,E

    ni = i+1
    nj = j
    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != v and arr[ni][nj] != node:
        if arr[ni][nj] == 0:
            d += 1
            down(ni, nj, node)
        else:
            if d>1 and node < arr[ni][nj] and not [node, arr[ni][nj], d] in res:
                E += 1
                res.append([node, arr[ni][nj], d])
            return

def right(i, j, node):
    global r,E

    ni = i
    nj = j+1
    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != v and arr[ni][nj] != node:
        if arr[ni][nj] == 0:
            r += 1
            right(ni, nj, node)
        else:
            if r>1 and node < arr[ni][nj] and not [node, arr[ni][nj], r] in res:
                E += 1
                res.append([node, arr[ni][nj], r])
            return

def left(i, j, node):
    global l,E

    ni = i
    nj = j-1
    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != v and arr[ni][nj] != node:
        if arr[ni][nj] == 0:
            l += 1
            left(ni, nj, node)
        else:
            if l>1 and node < arr[ni][nj] and not [node, arr[ni][nj], l] in res:
                E += 1
                res.append([node, arr[ni][nj], l])
            return


def bfs(i,j):
    global length_Islands

    island = [[i,j]]
    q = [[i,j]]
    while q:
        qo=q.pop(0)
        i = qo[0]
        j = qo[1]
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M:
                if visited[ni][nj]==0:
                    if arr[ni][nj]==0 and not [i,j] in island:
                        island.append([i,j])
                    elif arr[ni][nj]==1:
                        arr[ni][nj] = n
                        visited[ni][nj] = 1
                        q.append([ni,nj])
            else:
                if not [i,j] in island:
                    island.append([i,j])
    length_Islands += 1
    islands.append(island)



di,dj = [0,1,0,-1],[1,0,-1,0]
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

length_Islands = 0
visited = [[0]*M for i in range(N)]
islands = []
n = 1
v = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1
            arr[i][j] = n
            bfs(i,j)
            n += 1

v = 2
E = 0
res = []
for i in range(length_Islands):
    for x,y in islands[i]:
        visited[x][y] =v
        u,d,r,l=0,0,0,0
        up(x,y,arr[x][y])
        down(x,y,arr[x][y])
        right(x,y,arr[x][y])
        left(x,y,arr[x][y])
        v += 1

if E == 0 or E < n-2:
    print(-1)
else:
    i = 0
    while i < E-1:
        j = i+1
        a,b,c = res[i]
        while j < E:
            x,y,z = res[j]
            if a == x and y == b:
                if c < z:
                    res.pop(j)
                    E -= 1
                else:
                    j += 1
            else:
                j += 1
            if a != x:
                break

        i += 1


    res.sort(key=lambda x:x[2])

    p = [i for i in range(n)]
    disjoint = [0]*n

    minV = 0
    cnt = 0
    while cnt != n-1 and res:
        i,j,m = res.pop(0)
        ni,nj = find(i),find(j)
        if ni != nj:
            union(ni,nj)
            cnt += 1
            minV += m

    check = []
    ch = 0
    for i in range(1,n):
        while p[i] != i:
            i = p[p[i]]
        check.append(p[i])
        ch += 1
        if ch>1 and p[i] != check[-2]:
            minV = -1
            break

    print(minV)