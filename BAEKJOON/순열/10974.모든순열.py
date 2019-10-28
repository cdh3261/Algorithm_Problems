def f(n,k):

    if n==k:
        print(' '.join(map(str, p)))
    else:
        for m in range(N):
            if used[m] == 0:
                used[m] = 1
                p[n] = m+1
                f(n+1,k)
                used[m] = 0

N=int(input())
used = [0]*N
p = [0]*N
f(0,N)