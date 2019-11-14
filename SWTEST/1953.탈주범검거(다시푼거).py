import sys
sys.stdin = open('탈주범.txt','r')

def f(i, j):
    c = 1
    while q:
        qo = q.pop(0)
        i, j, n = qo[0], qo[1], qo[2]
        if visited[i][j] < L:
            for k in now[n]:
                ni = i+di[k]
                nj = j+dj[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] in next[k] and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j]+1
                    c += 1
                    q.append([ni, nj, arr[ni][nj]-1])
    print('#{} {}'.format(t+1, c))


now = [[0, 1, 2, 3], [3, 1], [2, 0], [3, 0], [0, 1], [1, 2], [3, 2]]
next = [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
for t in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    q = [[R, C, arr[R][C]-1]]
    visited = [[0]*M for i in range(N)]
    visited[R][C] = 1
    f(R, C)