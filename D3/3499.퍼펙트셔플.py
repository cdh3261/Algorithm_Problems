for tc in range(int(input())):
    N = int(input())
    t = input().split()

    res = []
    # N이 홀수이면 짝홀짝홀- 순서가 된다.
    if N % 2:
        fir = t[:(N // 2) + 1]
        sec = t[(N // 2) + 1:]
        for i in range(N):
            if i % 2:
                res.append(sec[i // 2])
            else:
                res.append(fir[i // 2])

    # N이 짝수이면 홀짝홀짝- 순서가 된다.
    else:
        fir = t[:(N // 2)]
        sec = t[(N // 2):]
        for i in range(N):
            if i % 2:
                res.append(sec[i // 2])
            else:
                res.append(fir[i // 2])
    print('#{} {}'.format(tc + 1, " ".join(res)))