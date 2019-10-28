def escape(Rx,Ry,Bx,By):
    global game, cnt, minV

    stack = []
    stack.append([Rx, Ry])

    while stack:
        st = stack.pop()
        i = st[0]
        j = st[1]
        for k in range(4):


            if cnt >= minV:
                break

            while 1:
                ni = i + di[k]
                nj = j + dj[k]

                # 오른쪽갈때
                if k == 0:
                    if 'B' in game[i][j+1:]:

                    else:
                        if game[ni][nj] == '#' or game[ni][nj] == 'B':
                            break
                        elif game[ni][nj] == 'O':
                            if cnt < minV:
                                minV = cnt

                        i += di[k]
                        j += dj[k]

                # 왼쪽
                if k == 1:
                    if 'B' in game[i][1:j]:

                    else:
                        if game[ni][nj] == '#' or game[ni][nj] == 'B':
                            break

                        elif game[ni][nj] == 'O':
                            if cnt < minV:
                                minV = cnt

                        i += di[k]
                        j += dj[k]

                # 아래
                if k == 2:
                      if 'B' in game[]

            cnt += 1
            stack.append([i, j])

di = [0,0,1,-1]
dj = [1,-1,0,0]

# R이 벽 or B를 만나면 방향 전환하면서 cnt +1
# R이 B보다 먼저 구멍을 만나면 끝.
# cnt>10이거나 B가 먼저 구멍을 만나면 -1 출력
N, M = map(int, input().split())
game = [list(input()) for i in range(N)]

for i in range(1,N-1):
    for j in range(1,M-1):
        if game[i][j] == 'B':
            Bx, By = i, j
        elif game[i][j] == 'R':
            Rx, Ry = i, j
cnt = 1
minV = float('INF')
# B의 좌표와 R의 좌표를 가지고 이동한다.
escape(Rx, Ry, Bx, By)
print(minV)