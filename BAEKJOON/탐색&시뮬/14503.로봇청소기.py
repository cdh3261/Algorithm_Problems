# 0 위, 1 오른쪽, 2 아래, 3 왼쪽
# 현재 위치를 청소한다.
# 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
# 1.왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 2.왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
# arr의 1은 벽, 0은 통로

def f(ar,a,b):
    global cnt, d, i, j

    c = True

    for di, dj in ar:
        ni, nj = i + di, j + dj
        d -= 1
        if d == -1:
            d = 3

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = 3
            cnt += 1
            i, j = ni, nj
            c = False
            break

    if c:
        ni, nj = a, b
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == 1:
                return 1
            elif arr[ni][nj] == 3:
                i, j = ni, nj


N,M = map(int, input().split())
i,j,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
arr[i][j] = 3
while 1:
    if d == 0:
        if f([(0,-1), (1,0), (0,1), (-1,0)],i+1,j):
            break
    elif d == 1:
        if f([(-1,0), (0,-1), (1,0), (0,1)],i,j-1):
            break
    elif d == 2:
        if f([(0, 1), (-1, 0), (0, -1), (1, 0)],i-1,j):
            break
    else:
        if f([(1, 0), (0, 1), (-1, 0), (0, -1)],i,j+1):
            break
print(cnt)