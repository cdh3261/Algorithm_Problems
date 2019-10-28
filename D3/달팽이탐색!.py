di = [0,1,0,1]
dj = [1,0,-1,0]

for tc in range(int(input())):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    dir = 0

    i = 0
    j = 0
    k = 1
    while k <= 9:
        arr[i][j] = k
        k += 1
        ni = i + di[dir]
        nj = j + dj[dir]
        if ni >= 0 and ni < N and nj >= 0 and nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir+1) % 4
            i += di[dir]
            j += dj[dir]