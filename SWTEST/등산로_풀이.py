import sys
sys.stdin = open('mount.txt', 'r')

def walking(i,j,c,e):
    global maxV

    maxV = max(maxV,e)
    visited[i][j] = 1

    for s in range(4):
        ni = i + di[s]
        nj = j + dj[s]
        if nj >= 0 and ni >= 0 and ni < N and nj < N:
            if mount[ni][nj] < mount[i][j]:
                walking(ni, nj, c, e + 1)
            elif visited[ni][nj] == 0 and c>0 and mount[i][j]>mount[ni][nj]-K: # 깍아서 더 낮아지는 경우
                org = mount[ni][nj] # 원래 높이
                mount[ni][nj] = mount[i][j] - 1 # 주변 칸을 깍아서 이동
                walking(ni, nj, 0, e+1)
                mount[ni][nj] = org # 돌아오면 높이 원상복구
    visited[i][j] = 0 # 다른 경로의 등산로에 포함될 수 있으므로 해제

di,dj = [0,1,0,-1],[1,0,-1,0]
for t in range(int(input())):
    N, K = map(int, input().split())
    maxV = 0
    mount = [list(map(int, input().split())) for i in range(N)]
    visited = [[0] * N for _ in range(N)]
    m = 0
    for i in range(N):
        for j in range(N):
            if mount[i][j] > m:
                m = mount[i][j]

    for i in range(N):
        for j in range(N):
            if mount[i][j] == m:
                walking(i,j,1,1)
    print('#{} {}'.format(t+1,maxV))