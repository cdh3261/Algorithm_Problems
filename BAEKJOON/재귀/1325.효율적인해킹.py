def f(x,y):


    for i in range(M):
        if y != i and arr[i][1] == y and visited[y] == 0:
            visited[arr[i][0]] = 1
            f(arr[i][0],arr[i][1])


N,M = map(int,input())
arr = [list(map(int,input().split())) for i in range(M)]

visited = [0]*(N+1)
for i in range(M):
    start = arr[i][1]
    visited[arr[i][0]] = 1
    f(arr[i][0],arr[i][1])