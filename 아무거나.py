


keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
# .복도 #벽 a-f열쇠 A-F문 0현재위치 1출구
N, M = map(int, input().split())
arr = [list(input()) for i in range(N)]

minV = float('INF')
find_keys = []
v = 1
cnt = 0
visited = [[[0]*64 for _ in range(M)] for _ in range(N)]
ju = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            arr[i][j] = '.'

            ju = False
            break
    if ju == False:
        break