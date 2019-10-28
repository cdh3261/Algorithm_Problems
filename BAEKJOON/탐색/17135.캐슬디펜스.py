def f(i,j):

    q = []
    q.append([i, j])





# 행,렬,사거리
N, M, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)] + [[0]*M]

# M까지의 수 중에서 3개 조합(궁수의 위치)
res = []
for i in range(1<<M):
    r = []
    for j in range(M):
        if i & (1<<j) != 0:
            r.append(j)
    if len(r)==3:
        res.append(r)

for i in range(len(res)):
    arr[N][res[i][0]] = 'archer'
    arr[N][res[i][1]] = 'archer'
    arr[N][res[i][2]] = 'archer'
    for j in range(3):
        f(N,res[i][j])
    arr[N][res[i][0]] = 0
    arr[N][res[i][1]] = 0
    arr[N][res[i][2]] = 0