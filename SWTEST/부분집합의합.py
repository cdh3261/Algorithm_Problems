def f(n,k,s,c):
    global cnt

    if s > V or c > N:
        return

    if s == V and c == N:
        cnt += 1
        return

    if n == k:
        return
    else:
        f(n+1,k,s+nums[n],c+1)
        f(n+1,k,s,c)

for t in range(int(input())):
    N,V=map(int,input().split())
    nums = [i for i in range(1,13)]
    cnt = 0
    f(0,12,0,0)
    print('#{} {}'.format(t+1,cnt))