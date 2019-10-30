def f(i,j,k):
    global axis,p


    while 1:

        if k == 0:
            ni = i + di[k]
            nj = j + dj[k]

            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == 1:
                    return






di,dj = [0,1,0,-1],[1,0,-1,0]
for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    axis = []
    c = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j] == 1:
                axis.append([i,j])
                c += 1

    p = [0]*c
    i,j=axis.pop(0)
    for k in range(4):
        f(i,j,k)