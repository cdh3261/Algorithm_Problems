import sys
sys.stdin = open('세포.txt', 'r')

def f(i,j):
    global cells,minV,re

    for time in range(minV,K):
        q,l = [],0
        while l != len(re):
            if re[l][4]==time:
                q.append([re[l][0], re[l][1], re[l][2], re[l][3], re[l][4]])
                re.pop(l)
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

                    else :
                        if cells[ni][nj][2] == time and cells[ni][nj][3]<life: #같은 시간에 들어오면
                            cells[ni][nj] = [ni,nj,time,life,time+life+1]
                            re.append([ni,nj,time,life,time+life+1])


di,dj=[0,1,0,-1],[1,0,-1,0]
for t in range(int(input())):
    N,M,K = map(int,input().split())

    cells = [[0]*(K+K+M) for _ in range(K)]+[[0]*K+list(map(int,input().split()))+[0]*K for _ in range(N)]+[[0]*(K+K+M) for _ in range(K)]
    #[K,K : K+N,K+M]까지 세포가 있다.
    re = []
    minV = float('INF')
    for i in range(K,K+N):
        for j in range(K,K+M):
            if cells[i][j]>0:
                if minV > cells[i][j]:
                    minV = cells[i][j]
                    I, J = i, j
                re.append([i, j, 0, cells[i][j], cells[i][j]])
                cells[i][j] = [i, j, 0, cells[i][j], cells[i][j]]
    # 마지막 - 활성화되는시간
    f(I,J)

    cnt = 0
    for i in range(K+K+N):
        for j in range(K+K+M):
            if cells[i][j]!=0 and (cells[i][j][3]+cells[i][j][4]>K or cells[i][j][3]+cells[i][j][2]>K):
                cnt += 1

    print('#{} {}'.format(t+1,cnt))