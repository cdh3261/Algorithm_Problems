def buy(i, j, go):
    global ladder, visited, cnt

    visited[i][j] = 1
    for di, dj in (0, -1), (0, 1), (1, 0):
        ni = i + di
        nj = j + dj

        if ni >= 0 and ni < 100 and nj >= 0 and nj < 100:
            if ladder[ni][nj] != 0 and visited[ni][nj] == 0:
                cnt += 1
                return buy(ni, nj, go)
    return cnt

for t in range(10):
    tc = input()

    ladder = [list(map(int, input().split())) for i in range(100)]
    s = float('inf')
    x_axis = 0
    for i in range(100):
        if ladder[0][i] == 1:
            cnt = 0
            visited = [[0]*100 for z in range(100)]
            I = 0
            J = i
            go = J
            if buy(I, J, go)<=s:
                s = cnt
                x_axis = J

    print('#{} {}'.format(tc, x_axis))