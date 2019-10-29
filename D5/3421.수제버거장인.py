def ncr(n,k):
    global cnt

    for i in range(M):
        if nums[arr[i][0]-1] == 1 and nums[arr[i][1]-1] == 1:
            return

    if n==k:
        cnt += 1
        return

    nums[n] = 1
    ncr(n+1,k)
    nums[n] = 0
    ncr(n+1,k)


for t in range(int(input())):
    N,M=map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(M)]
    nums = list(range(1,N+1))
    cnt = 0
    ncr(0,N)
    print('#{} {}'.format(t+1, cnt))