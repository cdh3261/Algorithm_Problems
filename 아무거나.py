def f(x,y,k):

    nx = x+dx[k]
    ny = y+dy[k]

    if 0<=nx<N and 0<=ny<N:
        if arr[nx][ny] == 0:
            case[j][0][0],case[j][0][1] = nx,ny
        elif arr[nx][ny] == 2:
            k += 1
            if k == 4:
                k = 0
            case[j][0][2] = k
        elif arr[nx][ny] == 1:
            case[j] = case[j][::-1]

        else:
            arr[x][y] = 0
            case[j].pop()
            for z in range(K):
                






N,K = map(int,input().split())
arr = list(map(int,input().split()))
# 0 흰색, 1 빨강, 2 파랑

# 오른쪽,왼쪽,위,아래
dx,dy=[0,0,-1,1],[1,-1,0,0]

case = [[]*K for i in range(K)]
for i in range(K):
    x,y,k = map(int,input().split())
    x,y,k = x-1,y-1,k-1
    arr[x][y] = [x,y,k]
    case[i].append([x,y,k]) # 좌표, n번 말, 방향을 넣어준다.

for i in range(1000):
    j = 0
    while j != K:
        f(case[j][0][0], case[j][0][1], case[j][0][2])
        j += 1