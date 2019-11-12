for t in range(int(input())):
    N,K = map(int, input().split())
    size = []
    value = []
    for _ in range(N):
        a,b = map(int,input().split())
        size.append(a)
        value.append(b)

    arr = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for s in range(1, K+1):
            if size[i-1]>s:
                arr[i][s] = arr[i-1][s]
            else:
                arr[i][s] = max(value[i-1]+arr[i-1][s-size[i-1]],arr[i-1][s])

    print('#{} {}'.format(t+1, arr[-1][-1]))