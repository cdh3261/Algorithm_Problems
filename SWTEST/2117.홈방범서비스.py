for t in range(int(input())) :
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    homes = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
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

                s -= distance[k-1]


    print('#{} {}'.format(t+1,maxV))


# 내포쓰기
# V = [0]*39
# V[0],V[1],V[2],V[3] = 1,5,13,25
# for i in range(4,40):
#     V[i] = i*i + (i-1)*(i-1)

# for t in range(int(input())) :
#     N,M = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     homes = [[i,j] for i in range(N) for j in range(N) if arr[i][j]]
#
#     maxV = 0
#     for i in range(N):
#         for j in range(N):
#             D = [0]*((2*N)-1)
#
#             for x,y in homes:
#                 D[abs(i-x)+abs(j-y)] += 1
#
#             s = sum(D)
#             for k in range(2*N-1,0,-1):
#                 if s*M-((k*k)+(k-1)*(k-1)) >= 0 and maxV<s:
#                     maxV=s
#                 s -= D[k-1]
#
#     print('#{} {}'.format(t+1,maxV))