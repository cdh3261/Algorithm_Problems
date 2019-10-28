for t in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int,input().split())))[::-1]
    s = 0
    for i in range(N):
        if (i+1)%3 != 0:
            s += arr[i]
    print('#{} {}'.format(t+1, s))