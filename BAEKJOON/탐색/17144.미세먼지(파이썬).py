def f(B,c):
    if c == 1:
        for x in range(B-1,0,-1):
            arr[x][0] = arr[x-1][0]
        for y in range(M-1):
            arr[0][y] = arr[0][y+1]
        for x in range(B):
            arr[x][M-1] = arr[x+1][M-1]
        for y in range(M-1,1,-1):
            arr[B][y] = arr[B][y-1]
    else:
        for x in range(B+1, N-1):
            arr[x][0] = arr[x+1][0]
        for y in range(M-1):
            arr[N-1][y] = arr[N-1][y+1]
        for x in range(N-1, B, -1):
            arr[x][M-1] = arr[x-1][M-1]
        for y in range(M-1, 1, -1):
            arr[B][y] = arr[B][y-1]
    arr[B][1] = 0

def spreadDust(): #확산
    move = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 5:
                d = arr[i][j] // 5
                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1:
                        move[ni][nj] += d
                        arr[i][j] -= d
    for i in range(N):
        for j in range(M):
            arr[i][j] += move[i][j]

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

robot = [[i,0,0] for i in range(N) if arr[i][0] == -1]
robot[1][2] = 2

for time in range(T):

    spreadDust()
    f(robot[0][0],1)
    f(robot[1][0],2)
arr[robot[0][0]][robot[0][1]] = 0
arr[robot[1][0]][robot[1][1]] = 0
print(sum(map(sum, arr)))