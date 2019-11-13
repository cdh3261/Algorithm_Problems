def npr(n, k, s):
    global oper, minV, maxV

    if n == k:
        minV = min(minV, s)
        maxV = max(maxV, s)
    else:
        if oper[0] != 0:
            oper[0] -= 1
            npr(n+1, k, s+nums[n])
            oper[0] += 1
        if oper[1] != 0:
            oper[1] -= 1
            npr(n+1, k, s-nums[n])
            oper[1] += 1
        if oper[2] != 0:
            oper[2] -= 1
            npr(n+1, k, s*nums[n])
            oper[2] += 1
        if oper[3] != 0:
            oper[3] -= 1
            npr(n+1, k, int(s/nums[n]))
            oper[3] += 1


for t in range(int(input())):
    N = int(input())
    oper = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    minV = float('INF')
    maxV = -float('INF')
    npr(1, N, nums[0])
    print('#{} {}'.format(t+1, maxV-minV))