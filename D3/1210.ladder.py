def buy(i, j, go):
    global ladder
    global visited

    if ladder[i][j] == 2:
        return go

    visited[i][j] = 1
    for di, dj in (0, -1), (0, 1), (1, 0):
        ni = i + di
        nj = j + dj

        if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] != 0 and visited[ni][nj] == 0:
            return buy(ni, nj, go)
    return 0

for t in range(10):
    t = input()

    ladder = [list(map(int, input().split())) for i in range(100)]

    res = 0
    for i in range(100):
        if ladder[0][i] == 1:
            visited = [[0]*100 for z in range(100)]
            I = 0
            J = i
            go = J
            res += buy(I, J, go)
        if res != 0:
            break
    print(f'#{t} {res}')