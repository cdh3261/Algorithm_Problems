N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [0]*N
for i in range(N-1,0,-1):
    for j in range(len(arr[i])-1):
        arr[i-1][j] += max(arr[i][j], arr[i][j+1])
print(arr[0][0])