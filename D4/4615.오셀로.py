def load(x, y, N, n, l):
    global othello
    nx = x + dx[l]
    ny = y + dy[l]
    if nx >= 0 and ny >= 0 and nx < N and ny < N:
        if othello[nx][ny] == n: # 다음 수가 자기 자신이면 0을 리턴한다.
            return 0
        elif othello[nx][ny] != n and othello[nx][ny] != 0:

            if load(nx, ny, N, n, l) == 0:  # 리턴 값이 0이면 그 위치의 값을 n으로 바꾼다.
                othello[nx][ny] = n
                return 0
            else:                           # 리턴 값이 1이거나 없으면 그냥 그대로 둔다.
                return 1

def find_my_load(x, y, N, n):
    global othello
    othello[x][y] = n
    stack = []
    stack.append([x, y])

    while stack:
        go = stack.pop()
        x = go[0]
        y = go[1]

        for k in range(8):  # 주변 8방향을 봐야 한다.
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if othello[nx][ny] != n and othello[nx][ny] != 0:
                    l = k
                    load(x, y, N, n, l)


# 9시방향부터 시계방향으로 본다.
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for t in range(int(input())):

    N, M = map(int, input().split())  # NxN행렬, M = 돌 놓는 횟수
    othello = [[0] * N for i in range(N)]  # 오셀로 판을 만든다.

    # 가운데 4부분은 초기값이 정해져있다.
    othello[N//2 - 1][N//2 - 1] = 2
    othello[N//2][N//2] = 2
    othello[N//2 - 1][N//2] = 1
    othello[N//2][N//2 - 1] = 1

    for i in range(M):
        x, y, n = map(int, input().split())  # 3 2 1 이면 (3,2)에 1번(백돌)을 놓는다.
        x -= 1
        y -= 1

        find_my_load(x, y, N, n)

    one = 0
    two = 0
    for j in range(N):
        one += othello[j].count(1)
        two += othello[j].count(2)
    print('#{} {} {}'.format(t + 1, one, two))