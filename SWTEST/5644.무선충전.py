import sys
sys.stdin = open('무선충전.txt', 'r')

# 상 1, 우 2, 하 3, 좌 4, 이동하지않는다 0
di = [0,-1,0,1,0]
dj = [0,0,1,0,-1]
for t in range(int(input())):

    # 총 이동시간(M), 충전소 갯수(A)
    M, A = map(int, input().split())

    # 0초부터 충전가능하므로
    moveA = [0]+list(map(int, input().split()))
    moveB = [0]+list(map(int, input().split()))

    # x,y 좌표, c 충전범위, p 충전량
    charge = []
    for i in range(A):
        y, x, c, p = map(int, input().split())
        x, y = x-1, y-1
        charge.append([x, y, c, p])

    chargeA = [[0]*(A+1) for _ in range(M+1)]
    chargeB = [[0]*(A+1) for _ in range(M+1)]
    A_x, A_y = 0,0
    B_x, B_y = 9,9
    for i in range(M+1):
        A_x += di[moveA[i]]
        A_y += dj[moveA[i]]
        B_x += di[moveB[i]]
        B_y += dj[moveB[i]]
        idx = 0
        for a,b,c,d in charge:
            distance_A = abs(A_x-a)+abs(A_y-b)
            distance_B = abs(B_x-a)+abs(B_y-b)
            if distance_A <= c:
                chargeA[i][idx] = d
            if distance_B <= c:
                chargeB[i][idx] = d
            idx += 1

    Asum, Bsum = 0, 0
    for i in range(M+1):
        Amax, Bmax = max(chargeA[i]), max(chargeB[i])

        if Amax == 0 or Bmax == 0:
            Bsum += Bmax
            Asum += Amax

        elif Amax == Bmax:
            if chargeA[i].index(Amax) != chargeB[i].index(Bmax):
                Asum += Amax
                Bsum += Bmax
            else:
                chargeA[i].pop(chargeA[i].index(Amax))
                chargeB[i].pop(chargeB[i].index(Bmax))
                if max(chargeA[i]) > max(chargeB[i]):
                    Asum += max(chargeA[i])
                    Bsum += Amax
                else:
                    Asum += Bmax
                    Bsum += max(chargeB[i])
        else:
             Asum += Amax
             Bsum += Bmax

    print('#{} {}'.format(t+1, Asum+Bsum))