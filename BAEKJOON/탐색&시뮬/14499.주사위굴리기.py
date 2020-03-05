# 시작 : 12시 45분 /// 종료 : 13시 17분
# 동 1, 서 2, 북 3, 남 4

N,M,x,y,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
play = list(map(int,input().split()))

# 주사위 위에서부터 0,1,2,3 왼쪽 4 오른쪽 5번 지정.
dice = [0,0,0,0,0,0]
if arr[x][y] != 0:
    dice[1] = arr[x][y]
    arr[x][y] = 0

for i in play:
    if i == 1 and 0<=x<N and 0<=y+1<M:
        y = y+1
        dice[1],dice[3],dice[4],dice[5] = dice[5],dice[4],dice[1],dice[3]
        if arr[x][y] == 0:
            arr[x][y] = dice[1]
        else:
            dice[1] = arr[x][y]
            arr[x][y] = 0
        print(dice[3])

    elif i == 2 and 0<=x<N and 0<=y-1<M:
        y = y-1
        dice[1],dice[3],dice[4],dice[5] = dice[4],dice[5],dice[3],dice[1]
        if arr[x][y] == 0:
            arr[x][y] = dice[1]
        else:
            dice[1] = arr[x][y]
            arr[x][y] = 0
        print(dice[3])

    elif i == 3 and 0<=x-1<N and 0<=y<M:
        x = x-1
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]
        if arr[x][y] == 0:
            arr[x][y] = dice[1]
        else:
            dice[1] = arr[x][y]
            arr[x][y] = 0
        print(dice[3])

    elif i == 4 and 0<=x+1<N and 0<=y<M:
        x = x+1
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
        if arr[x][y] == 0:
            arr[x][y] = dice[1]
        else:
            dice[1] = arr[x][y]
            arr[x][y] = 0
        print(dice[3])