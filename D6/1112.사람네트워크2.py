import sys
sys.stdin = open('사람네트워크2.txt','r')

for t in range(int(input())):
    a = list(map(int,input().split()))
    N = a[0]
    M = N*N
    arr = [a[i*N+1:(i*N+1)+N] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = 1001

    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if j != k and j != i:
                        if arr[i][j] > arr[i][k]+arr[k][j]:
                            arr[i] [j] = arr[i][k]+arr[k][j]

    minV = 1000000000
    for i in range(N):
        s = 0
        for j in range(N):
            if arr[i][j] != 1001:
                s += arr[i][j]
                if s >= minV:
                    break
        minV = min(minV, s)

    print('#{} {}'.format(t+1,minV))