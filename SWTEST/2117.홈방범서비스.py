for t in range(int(input())) :
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    homes,cnt = [],0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                cnt+=1
                homes.append([i,j])
    maxV = 0
    for i in range(N):
        for j in range(N):
            distance = [0]*((2*N)-1)

            for x,y in homes:
                distance[abs(i-x)+abs(j-y)] += 1

            s = 0
            for l in distance:
                s += l

            for k in range(2*N-1,0,-1):
                if s*M-((k*k)+(k-1)*(k-1)) >= 0 and maxV<s:
                    maxV=s
                    if maxV==cnt:
                        break
                s -= distance[k-1]
            if maxV==cnt:
                break
        if maxV==cnt:
            break
    print('#{} {}'.format(t+1,maxV))