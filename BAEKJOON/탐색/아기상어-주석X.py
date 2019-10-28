def help_me_mom(i, j, shark):

    global fish_Tank, arr, N, cnt

    visited = [[0]*N for l in range(N)]
    q=[]
    q.append([i, j])
    visited[i][j] = 1
    fish_Find = [] # 먹을 수 있는 물고기의 좌표
    while q:
        if not fish_Find:
            for s in range(len(q)):
                qo = q.pop(0)
                i = qo[0]
                j = qo[1]

                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if ni >= 0 and nj >= 0 and ni < N and nj < N and visited[ni][nj] == 0 and fish_Tank[ni][nj] <= shark:
                        if 0 < fish_Tank[ni][nj] < shark:
                            arr[ni][nj] = arr[i][j] + 1
                            visited[ni][nj] = 1
                            fish_Find.append([ni, nj])
                        else:
                            arr[ni][nj] = arr[i][j] + 1
                            visited[ni][nj] = 1
                            q.append([ni, nj])
        else:
            break
    if fish_Find:
        fi = sorted(fish_Find).pop(0)
        fix = fi[0]
        fiy = fi[1]
        fish_Tank[fix][fiy] = 0
        time_Check.append(arr[fix][fiy])
        cnt += 1
        if cnt == shark:
            cnt = 0
            shark += 1
        help_me_mom(fix, fiy, shark)


di = [-1,0,0,1]
dj = [0,-1,1,0]

N = int(input())
fish_Tank = [list(map(int, input().split())) for i in range(N)]
arr = [[0]*N for i in range(N)]

shark = 2
cnt = 0
time_Check = [0]

I = -1
for i in range(N):
    for j in range(N):
        if fish_Tank[i][j] == 9:
            fish_Tank[i][j] = 0
            I, J = i, j
            help_me_mom(I, J, shark)
            break
    if I != -1:
        break

print(time_Check[-1])