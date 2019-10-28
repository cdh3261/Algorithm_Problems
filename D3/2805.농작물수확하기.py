for tc in range(int(input())):
    n = int(input())
    res = []
    for i in range(n):
        res.append(list(map(int, input())))
    cen = n//2
    cnt = 0
    for i in range(cen+1):
        if i != cen:
            cnt += sum(res[i][cen-i:cen+i+1])+sum(res[-i-1][cen-i:cen+i+1])
        else:
            cnt += sum(res[i])
    print(f'#{tc+1} {cnt}')