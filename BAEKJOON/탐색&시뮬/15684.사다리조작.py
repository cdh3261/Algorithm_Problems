N, M, H = map(int, input().split())
ladder = [[0]*N for i in range(H)]
for i in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 1
for i in range(N):
