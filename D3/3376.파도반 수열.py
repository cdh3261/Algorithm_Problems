for t in range(int(input())):
    N = int(input())
    l = [1,1,1,2,2]
    for i in range(5, N):
        l += [l[i-5] + l[i-1]]
    print('#{} {}'.format(t+1, l[N-1]))