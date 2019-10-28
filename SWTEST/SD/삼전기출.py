def f(i,j,k):
    global P,I,q,d1,d2

    dir=3
    while 1:
        ni=i+di[dir]
        nj=j+dj[dir]
        if 0<=ni<k and 0<=nj<k:
            q.append([ni+P,nj+I])
            i, j = ni, nj
            if dir == 3:
                d1 += 1
            elif dir == 2:
                d2 += 1
        elif nj==-1:
            dir = 2
        elif ni==k:
            dir = 1
        elif nj==k:
            dir = 0
        elif ni==-1:
            return

di,dj = [-1,-1,1,1],[-1,1,1,-1]
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

totalSum = 0
for i in range(N):
    totalSum += sum(arr[i])

V = float('INF')
for k in range(3,N+1):
    for p in range(N-k+1):
        for i in range(N-k+1):
            P,I=p,i

            for x in range(k):
                if x != 0 and x != k-1:
                    q, d1, d2 = [], 0, 0
                    s1, s2, s3, s4, s5 = 0, 0, 0, 0, 0
                    f(0, x, k)

                    for n in range(0,P+d1):
                        for m in range(0,x+i+1):
                            if [n,m] in q:
                                break
                            else:
                                s1 += arr[n][m]

                    for n in range(0,P+d2+1):
                        for m in range(N-1,x+i,-1):
                            if [n,m] in q:
                                break
                            else:
                                s2 += arr[n][m]

                    for n in range(P+d1,N):
                        for m in range(0,x+i-d1+d2):
                            if [n,m] in q:
                                break
                            else:
                                s3 += arr[n][m]

                    for n in range(P+d2+1,N):
                        for m in range(N-1,x+i-d1+d2-1,-1):
                            if [n,m] in q:
                                break
                            else:
                                s4 += arr[n][m]

                    s5 = totalSum-s1-s2-s3-s4
                    maxV = max(s1,s2,s3,s4,s5)
                    minV = min(s1,s2,s3,s4,s5)
                    if V>maxV-minV:
                        V=maxV-minV
print(V)