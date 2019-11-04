H,W = map(int,input().split())
arr = [list(input()) for i in range(H)]
res = [[-1]*W for i in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            res[i][j] = 0
        else:
            cnt = 1
            nj = j - 1
            while 0<=nj:
                if arr[i][nj] == 'c':
                    res[i][j] = cnt
                    break
                cnt += 1
                nj -= 1
for i in range(H):
    print(' '.join(map(str, res[i])))