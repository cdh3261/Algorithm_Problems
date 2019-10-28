def f(ch, th):
    global minV, res

    if th >= re + 1:
        return

    for z in range(W):
        res[pos[th]][z] = ch

    if th == re:
        cnt = 0
        for i in range(W):
            for j in range(D - (K - 1)):
                s = 0
                for m in range(K):
                    s += res[j + m][i]
                if s == 0 or s == K:
                    cnt += 1
                    break
            if cnt + (W - i - 1) != W:
                break
        if cnt == W:
            if minV > re + 1:
                minV = re + 1
            return 1

    if f(0, th + 1) == 1:
        return 1
    if f(1, th + 1) == 1:
        return 1


for t in range(int(input())):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    cnt = 0
    for i in range(W):
        for j in range(D - (K - 1)):
            s = 0
            for m in range(K):
                s += arr[j + m][i]
            if s == 0 or s == K:
                cnt += 1
                break
    if cnt == W:
        print('#{} 0'.format(t + 1))
    else:
        minV = float('INF')
        jud = False

        for i in range(1, 1 << D):
            pos = [0] * K
            re = -1
            for j in range(D):
                if i & (1 << j) != 0:
                    re += 1
                    pos[re] = j
                    if re >= K - 1:
                        break

            if re < minV:
                res = [0] * D
                a = -1
                for x in range(D):
                    r = [0] * W
                    b = -1
                    for y in range(W):
                        b += 1
                        r[b] = arr[x][y]
                    a += 1
                    res[a] = r
                f(0, 0)
                f(1, 0)
            else:
                break

        print('#{} {}'.format(t + 1, minV))