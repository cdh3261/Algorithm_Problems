import sys
sys.stdin = open('정비소.txt','r')

for tc in range(int(input())):
    N, M, K, A, B = map(int, input().split())

    register = [0] + list(map(int, input().split()))
    repair = [0] + list(map(int, input().split()))
    arrive_time = [0] + list(map(int, input().split()))

    register_waitting = [[0] for _ in range(N+1)]
    repair_waitting = [[0] for _ in range(M+1)]

    register_total_waitting = []
    i = 1
    while i != K+1:
        minV = float('INF')
        for z in range(1, N+1):
            if arrive_time[i] - register_waitting[z][-1] >= 0:
                idx = z
                break
            if minV > register_waitting[z][-1]:
                minV = register_waitting[z][-1]
                idx = z
        if register_waitting[idx][-1] < arrive_time[i]:
            V = arrive_time[i] + register[idx]
        else:
            V = register_waitting[idx][-1] + register[idx]

        register_waitting[idx] += [i, V]
        register_total_waitting += [[idx, i, V]]
        i += 1

    register_total_waitting.sort(key=lambda x: (x[2], x[0]))

    i,s = 1,0
    while i != K + 1:
        minV = float('INF')
        for z in range(1, M + 1):
            if register_total_waitting[i - 1][-1] - repair_waitting[z][-1] >= 0:
                idx = z
                break
            if minV > repair_waitting[z][-1]:
                minV = repair_waitting[z][-1]
                idx = z
        if repair_waitting[idx][-1] < register_total_waitting[i - 1][-1]:
            V = register_total_waitting[i - 1][-1] + repair[idx]
        else:
            V = repair_waitting[idx][-1] + repair[idx]
        repair_waitting[idx] += [i, V]

        if register_total_waitting[i-1][0]==A and idx==B:
            s += register_total_waitting[i-1][1]
        i += 1

    if s == 0:
        s = -1
    print('#{} {}'.format(tc + 1, s))