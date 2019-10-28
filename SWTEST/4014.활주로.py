import sys
sys.stdin = open('활주로.txt','r')
for t in range(int(input())):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    col = list(zip(*arr))

    s = 0
    for i in range(N):
        jud,jud2 = False,False
        res,res2 = [],[]
        cnt,cnt2 = 1,1
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
                if j == N-2:
                    res.append([arr[i][j], cnt])
                    cnt = 1
            else:
                res.append([arr[i][j], cnt])
                if j == N-2:
                    res.append([arr[i][j+1], 1])
                cnt = 1
            if col[i][j] == col[i][j+1]:
                cnt2 += 1
                if j == N-2:
                    res2.append([col[i][j], cnt2])
                    cnt2 = 1
            else:
                res2.append([col[i][j], cnt2])
                if j == N-2:
                    res2.append([col[i][j+1], 1])
                cnt2 = 1
        if len(res) == 1:
            jud = True
        else:
            for k in range(len(res)-1):
                if res[k+1][0] - res[k][0] == 1 and res[k][1] >= X:
                    jud = True
                elif res[k][0] - res[k+1][0] == 1 and res[k+1][1] >= X:
                    jud = True
                    res[k+1][1] -= X
                else:
                    jud = False
                    break
        if len(res2)==1:
            jud2 = True
        else:
            for k in range(len(res2)-1):
                if res2[k+1][0] - res2[k][0] == 1 and res2[k][1] >= X:
                    jud2 = True
                elif res2[k][0] - res2[k+1][0] == 1 and res2[k+1][1] >= X:
                    jud2 = True
                    res2[k+1][1] -= X
                else:
                    jud2 = False
                    break
        if jud:
            s += 1
        if jud2:
            s += 1
    print('#{} {}'.format(t+1, s))