import sys
sys.stdin = open('핀볼.txt', 'r')

def f(i,j,k):
    global cnt

    start,end = i,j
    while 1:
        ni = i + di[k]
        nj = j + dj[k]
        if ni==start and nj==end:
            return
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] >=6:
                for x in range(len(holl)):
                    if holl[x][2]==arr[ni][nj] and (holl[x][0]!=ni or holl[x][1]!= nj):
                        i,j = holl[x][0],holl[x][1]
            elif arr[ni][nj] == 0:
                i,j=ni,nj
            elif arr[ni][nj] == -1:
                return
            else:
                k = kth[arr[ni][nj]-1][k]
                i,j=ni,nj
                cnt += 1
        else:
            k = 3-k
            cnt += 1
            i,j = ni,nj

kth = [[3,0,1,2],[3,2,0,1],[1,2,3,0],[2,3,1,0],[3,2,1,0]]
di,dj = [0,1,-1,0],[1,0,0,-1]
for t in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    startPoint = [0]*100*100*4
    r=-1
    holl = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 6:
                holl.append([i, j, arr[i][j]])
            for k in range(4):
                if arr[i][j] == 0:
                    r += 1
                    startPoint[r] = [i,j,k]
    maxV = 0
    for a in range(r):
        i,j,k=startPoint[a]
        cnt = 0
        f(i,j,k)
        maxV = max(maxV,cnt)
    print('#{} {}'.format(t+1,maxV))