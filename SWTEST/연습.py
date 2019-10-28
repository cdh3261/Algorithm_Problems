import sys
sys.stdin = open('세포.txt', 'r')

def f(i,j):
    global cells,minV,re,rea,fro

    for time in range(minV,K):
        q = [0] * (rea+1)
        rear = front = -1
        for l in range(rea+1):
            if re[l][4] == time:
                rear+=1
                q[rear]=[re[l][0], re[l][1], re[l][2], re[l][3], re[l][4]]

        while rear!=front:
            front+=1
            i, j, made_time, life, total_time = q[front]
            I, J = i, j
            for k in range(4):
                ni=i+di[k]
                nj=j+dj[k]
                if 0<=ni<K+K+N and 0<=nj<K+K+M:
                    if cells[ni][nj]==0:
                        cells[ni][nj] = [ni,nj,time,life,time+life+1]
                        rea+=1
                        re[rea]=[ni,nj,time,life,time+life+1]

                    else :
                        if cells[ni][nj][2] == time:
                            if cells[ni][nj][3]<life:
                                cells[ni][nj] = [ni,nj,time,life,time+life+1]
                                rea+=1
                                re[rea]=[ni,nj,time,life,time+life+1]


di,dj=[0,1,0,-1],[1,0,-1,0]
for t in range(int(input())):
    N,M,K = map(int,input().split())

    cells = [[0]*(K+K+M) for _ in range(K)]+[[0]*K+list(map(int,input().split()))+[0]*K for _ in range(N)]+[[0]*(K+K+M) for _ in range(K)]

    re = [0]*(N+K+K)*(M+K+K)
    rea=fro=-1
    minV = float('INF')
    for i in range(K,K+N):
        for j in range(K,K+M):
            if cells[i][j]>0:
                if minV > cells[i][j]:
                    minV = cells[i][j]
                    I, J = i, j
                rea+=1
                re[rea]=[i, j, 0, cells[i][j], cells[i][j]]
                cells[i][j] = [i, j, 0, cells[i][j], cells[i][j]]

    f(I,J)

    cnt = 0
    for i in range(K+K+N):
        for j in range(K+K+M):
            if cells[i][j]!=0:
                # 활성
                if cells[i][j][3]+cells[i][j][4]>K:
                    cnt += 1
                # 비활성
                elif cells[i][j][3]+cells[i][j][2]>K:
                    cnt += 1
    print('#{} {}'.format(t+1,cnt))