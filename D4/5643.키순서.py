import sys
sys.stdin = open('키순서.txt', 'r')

for t in range(int(input())):
    N = int(input())
    M = int(input())
    arr = [[0]*N for i in range(N)]
    for i in range(M):
        a,b = map(int,input().split())
        arr[a-1][b-1] = 1

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for k in range(N):
                    if arr[j][k]:
                        arr[i][k] = 1

    cnt = 0
    for i in range(N):
        s = 0
        for j in range(N):
            s += arr[i][j]+arr[j][i]
        if s == N-1:
            cnt += 1

    print('#{} {}'.format(t+1,cnt))