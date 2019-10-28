# 1) 가는 길에 방문 표시를 한다.
# 2) 가는 길의 숫자를 더한다.
# 3) 4방향 중 작은 곳으로 간다...?(아닌 듯)
# 3) 우, 하 중 작은 곳으로 간다...?

def repair(i,j,N,s):
    global arr, jud

    # s => 가는 길의 합을 구함
    if i == N-1 and j == N-1 and s < jud:
        jud = s

    elif s >= jud:
        return

    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and nj >= 0 and ni < N and nj < N and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                repair(ni,nj,N,s+arr[ni][nj])
                visited[ni][nj] = 0


di = [0,1,0,-1]
dj = [1,0,-1,0]

TC = int(input())
for t in range(TC):
    N = int(input())

    arr = []
    for i in range(N):
        a = [int(j) for j in input()]
        arr.append(a)

    visited = [[0]*N for i in range(N)]
    visited[0][0] = 1  # 방문 표시
    jud = sum(arr[0])+sum(list(zip(*arr))[-1])-arr[0][-1] # ㄱ자를 더해 기준으로 생각한다.

    # 0,0 에서 N-1,N-1 까지
    repair(0,0,N,0)
    print('#{} {}'.format(t+1, jud))