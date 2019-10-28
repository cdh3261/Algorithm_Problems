def f(i, N):
    global col, cnt, board, left, right

    if i == N: # 모든 줄에 퀸을 놓으면
        cnt += 1
        for i in range(N):
            print(board[i])
        print('\n')
    else:

        # 다른 줄에 j번 열의 퀸이 없어야하고
        # 왼쪽 대각선, 오른쪽 대각선에 퀸이 없어야 한다.
        # j열에 놓을 수 있으면 다음 줄로 이동 f(i+1,N)
        for j in range(N):
            if col[j] == 0 and right[i+j]==0 and left[i-j+N-1]==0:
                board[i][j] = 1
                col[j] = 1 # 현재 줄에서 j열을 사용함으로 표시
                right[i+j] = 1
                left[i-j+N-1] = 1

                f(i+1, N)
                board[i][j] = 0
                col[j] = 0
                right[i+j] = 0
                left[i-j+N-1] = 0


for t in range(int(input())):
    N = int(input())
    board = [[0]*N for i in range(N)]
    col = [0]*N
    right = [0]*(2*N-1)
    left = [0]*(2*N-1)
    cnt = 0
    f(0,N)
    print(cnt)