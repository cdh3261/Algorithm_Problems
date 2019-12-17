N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
game = [list(map(int,input().split())) for _ in range(K)]

# 게임이 종료되는 턴의 번호 출력. 100보다 크거나 종료되지 않으면 -1 출력
# 흰색 0, 빨간 1, 파란 2
# 행, 열, 이동방향(1-4; 우좌상하)

# 말 번호 => 5,6,7,8 로 생각

num = 1
check = [[0]*N for _ in range(N)]
horse = [[],[],[],[]]
for i,j,k in game:
    horse[num-1].append([i-1,j-1,k,num])
    check[i-1][j-1] = 1
    num += 1

while 1:
    for m in range(1,5):
        i = game[m-1][0] - 1
        j = game[m-1][1] - 1
        k = game[m-1][2]
        if k == 1: # 오른쪽
            if j+1<N:

                # 흰색
                if arr[i][j+1] == 0 and check[i][j+1] == 0: #말이 없을 때
                    check[i][j], check[i][j+1] = 0, check[i][j]+1

                elif arr[i][j+1] == 0 and check[i][j+1] != 0: #말이 있을 때
                    check[i][j+1].append(check[i][j])
                    check[i][j] = 0

                # 빨간색
                elif arr[i][j+1] == 1 and check[i][j+1] == 0:
                    check[i][j+1] = check[i][j][::-1]
                    check[i][j] = 0
                elif arr[i][j+1] == 1 and check[i][j+1] != 0:
                    check[i][j+1].append(check[i][j][::-1])
                    check[i][j] = 0

                # 파란색
                elif arr[i][j+1] == 2:
                    if j-1 >= 0:
                        if arr[i][j-1] == 2:




            else:
