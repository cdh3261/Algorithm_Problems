def f(i,j,pos,p):
    start,end = i,j
    res,k = [],3
    while 1:
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<p and 0<=nj<p:
            if pos[ni][nj] in res:
                return 0
            i,j=ni,nj
            res.append(pos[ni][nj])
            if ni==start and nj==end:
                return len(res)
        elif nj==-1:
            k = 2
        elif ni==p:
            k = 1
        elif nj==p:
            k = 0

def d():
    global maxV
    for p in range(N,2,-1):
        for q in range(N-p+1):
            for i in range(N-p+1):
                pos = [0]*p
                for j in range(p):
                    pos[j] = arr[j+q][i:i+p]
                for y in range(p):
                    if not y == 0 and not y == p-1:
                        maxV = max(f(0,y,pos,p), maxV)
                    if maxV != 0:
                        return maxV

di,dj = [-1,-1,1,1],[-1,1,1,-1]
for t in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxV = 0
    if d() == None:
        maxV = -1
    print('#{} {}'.format(t+1, maxV))