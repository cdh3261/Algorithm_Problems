def combination(n,k,cnt):
    global total_wall, res, rear

    if cnt == 3:
        total_wall.append(res[:])
    elif n == k:
        return
    else:
        rear += 1
        res[rear] = possible_wall[n]
        combination(n+1, k, cnt+1)
        rear -= 1
        combination(n+1, k, cnt)

def virus(i,j):
    global arr,N,M

    rear = front = -1
    rear += 1
    q = [0]*N*M
    q[rear] = [i, j]
    while rear != front:
        front += 1
        qo = q[front]
        i = qo[0]
        j = qo[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 2
                    rear += 1
                    q[rear] = [ni, nj]


di=[0,1,0,-1]
dj=[1,0,-1,0]

N,M = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(N)]

possible_wall=[]
virus_location = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            possible_wall.append([i, j])
        elif lab[i][j] == 2:
            virus_location.append([i, j])

# 찾은 통로에서 조합으로 3개를 구한다.
total_wall = []
res = [0]*3
rear = -1
combination(0,len(possible_wall),0)
s = 0
for i in range(len(total_wall)):
    re = -1
    arr = [0]*N
    for j in range(N):
        re += 1
        arr[re] = lab[j][:]
    c = 0
    for j in range(3):
        arr[total_wall[i][j][0]][total_wall[i][j][1]] = 1
    for j in range(len(virus_location)):
        virus(virus_location[j][0], virus_location[j][1])
    for j in range(N):
        c += arr[j].count(0)
    if s < c:
        s = c
print(s)