TC = int(input())
for t in range(TC):
    N, X = map(int, input().split()) # N*N 행렬, X길이의 활주로
    arr = [list(map(int, input().split())) for i in range(N)]

    col = list(zip(*arr)) # 세로배열

    s = 0
    # 1) 가로
    for i in range(N):
        jud = False
        res = []
        cnt = 1
        for j in range(N-1): # X가 2이상이므로 끝은 안봐도 된다.

            if arr[i][j] == arr[i][j+1]: # 다음 수랑 같으면 cnt +1
                cnt += 1
                if j == N-2:    # 마지막의 하나 앞에서는 마지막 것도 같이 봐준다.
                    res.append([arr[i][j], cnt]) # 수와 그 수의 연달은 개수를 넣어준다. cnt는 1로 초기화
                    cnt = 1
            else:
                res.append([arr[i][j], cnt]) # 다음 수와 같지 않으면
                if j == N-2:
                    res.append([arr[i][j+1], 1])
                cnt = 1 # cnt는 1로 초기화
        if len(res) == 1: #res 길이가 1이라는 것은 행이 다 같은 숫자.
            jud = True
        else:
            for k in range(len(res)-1):
                if res[k+1][0] - res[k][0] == 1 and res[k][1] >= X:#뒤가 1 큰 수이면
                    jud = True
                elif res[k][0] - res[k+1][0] == 1 and res[k+1][1] >= X: #앞이 1 큰 수이면
                    jud = True
                    res[k+1][1] -= X # 활주로가 완성되면 그 만큼은 사용할 수 없으므로 빼준다.
                else:   # 1큰 수가 없거나 X보다 짧을 때
                    jud = False
                    break
        if jud:
            s += 1

    # 2) 세로
    for i in range(N):
        jud = False
        res = []
        cnt = 1
        for j in range(N-1):

            if col[i][j] == col[i][j+1]:
                cnt += 1
                if j == N-2:
                    res.append([col[i][j], cnt])
                    cnt = 1
            else:
                res.append([col[i][j], cnt])
                if j == N-2:
                    res.append([col[i][j+1], 1])
                cnt = 1
        if len(res) == 1:
            jud = True
        else:
            for k in range(len(res)-1):
                if res[k+1][0] - res[k][0] == 1 and res[k][1] >= X:
                    jud = True
                elif res[k][0] - res[k+1][0] == 1 and res[k+1][1] >= X:
                    jud = True
                    res[k + 1][1] -= X
                else:
                    jud = False
                    break
        if jud:
            s += 1

    print('#{} {}'.format(t+1, s))