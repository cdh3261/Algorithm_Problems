for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    minV = float('INF')
    for i in range(N):
        c = sum(a[:i+1])
        ab = c-(s-c)
        if ab<0:
            ab = -ab
        if minV>ab:
            minV = ab
            fir,sec = i+1, minV
    print('#%d %d %d' %(t+1,fir,sec))