import sys
sys.stdin = open('세포.txt', 'r')

def f(i,j):
    global cells,minV,re,lengthRE

    for time in range(minV,K):
        q,l = [],0

        while l != lengthRE:
            if re[l][4]==time:
                q.append([re[l][0], re[l][1], re[l][2], re[l][3], re[l][4]])
                re.pop(l)
                lengthRE -= 1
            else:
                l+=1

        while q:
            i, j, made_time, life, total_time = q.pop(0)
            I, J = i, j
            for k in range(4):
                ni=i+di[k]
                nj=j+dj[k]
                if 0<=ni<K+K+N and 0<=nj<K+K+M:
                    if cells[ni][nj]==0:
                        cells[ni][nj] = [ni,nj,time,life,time+life+1]
                        re.append([ni,nj,time,life,time+life+1])
                        lengthRE += 1

                    else :
                        if cells[ni][nj][2] == time and cells[ni][nj][3]<life:
                            cells[ni][nj] = [ni,nj,time,life,time+life+1]
                            re.append([ni,nj,time,life,time+life+1])
                            lengthRE += 1


di,dj=[0,1,0,-1],[1,0,-1,0]
for t in range(int(input())):
    N,M,K = map(int,input().split())

    cells = [[0]*(K+K+M) for _ in range(K)]+[[0]*K+list(map(int,input().split()))+[0]*K for _ in range(N)]+[[0]*(K+K+M) for _ in range(K)]
    re = []
    lengthRE = 0
    minV = float('INF')
    for i in range(K,K+N):
        for j in range(K,K+M):
            if cells[i][j]>0:
                if minV > cells[i][j]:
                    minV = cells[i][j]
                    I, J = i, j
                re.append([i, j, 0, cells[i][j], cells[i][j]])
                lengthRE += 1
                cells[i][j] = [i, j, 0, cells[i][j], cells[i][j]]
    f(I,J)

    cnt = 0
    for i in range(K+K+N):
        for j in range(K+K+M):
            if cells[i][j]!=0 and (cells[i][j][3]+cells[i][j][4]>K or cells[i][j][3]+cells[i][j][2]>K):
                cnt += 1

    print('#{} {}'.format(t+1,cnt))