def ncr(n,k,s):
    global cnt

    if s > K:
        return

    if n == k:
        if s == K:
            cnt += 1
        return

    ncr(n+1,k,s+arr[n])
    ncr(n+1,k,s)

for t in range(int(input())):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    ncr(0,N,0)
    print('#{} {}'.format(t+1, cnt))