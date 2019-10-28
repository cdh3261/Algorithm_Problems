# 상어는 자기보다 작은 물고기를 먹을 수 있다. 상어는 자기보다 작거나 같은 크기의 물고기 영역을 지날 수 있다.
# 상어는 1초에 상하좌우 1씩 이동할 수 있다.
# 같은 거리면 젤 위의 물고기를, 젤 위 물고기가 많으면 그 중 왼쪽을 먹는다.
# 자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가한다.
# 먹을게 없다면 끝

# 1)상어보다 작은 크기의 물고기 위치를 넣는다.
# 2)위치들 중에서 가까운 거리로 간다. (그 위치는 0이 된다. 거리를 더한다. 상어가 지나간 이전 위치는 0이 된다.)
# 3)상어의 크기의 물고기마리수를 먹으면 upgrade가 된다.

################################################################################
def help_me_mom(i, j, shark):

    global fish_Tank, arr, N, cnt

    visited = [[0]*N for l in range(N)]
    q=[]
    q.append([i, j])
    visited[i][j] = 1
    fish_Find = []
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
        time_Check.append(arr[fix][fiy]) # 먹은 물고기의 시간체크
        cnt += 1
        if cnt == shark:
            cnt = 0
            shark += 1
        help_me_mom(fix, fiy, shark)  # 먹은 물고기의 위치에서 다시 시작


di = [-1,0,0,1]
dj = [0,-1,1,0]

N = int(input()) # 공간의 크기 NxN
fish_Tank = [list(map(int, input().split())) for i in range(N)] # 9가 아기상어 위치
arr = [[0]*N for i in range(N)] # 시간을 구할 arr

shark = 2 # 아기 상어 크기
cnt = 0 # 아기 상어가 먹은 물고기 개수, upgrade되면 초기화를 해줘야 한다.
time_Check = [0]

I = -1
for i in range(N):
    for j in range(N):
        if fish_Tank[i][j] == 9: # 아기 상어 위치
            fish_Tank[i][j] = 0
            I, J = i, j
            help_me_mom(I, J, shark)
            break
    if I != -1:
        break

print(time_Check[-1])