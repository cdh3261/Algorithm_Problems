def npr(n,k,s):

    if s > 10:
        return

    if n==k:
        if s == 10:
            print(p)
        return
    else:
        for m in range(N):

            p[n] = nums[m]
            npr(n+1,k,s+nums[m])


nums = list(range(0,11))
N=11
used = [0]*N
p=[0]*4
npr(0,4,0)