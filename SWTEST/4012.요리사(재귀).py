import sys
sys.stdin = open('요리사.txt','r')

def ncr(n, k, cnt):
    global minV, c, case

    if c == case//2+2:
        return

    if cnt == N//2:
        c += 1
        s_man = list(nums-set(f_man))
        FV, SV = 0, 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                FV += arr[f_man[i]][f_man[j]]+arr[f_man[j]][f_man[i]]
                SV += arr[s_man[i]][s_man[j]]+arr[s_man[j]][s_man[i]]
        minV = min(minV, abs(FV-SV))
        return

    if n == k:
        return

    else:
        f_man[cnt] = n
        ncr(n+1, k, cnt+1)
        ncr(n+1, k, cnt)


for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = set(i for i in range(N))
    f_man = [0]*(N//2)
    minV = float('INF')
    case = 1
    for i in range(N, N//2, -1):
        case = case*i//(i-(N//2))
    c = 0
    ncr(0, N, 0)

    print('#{} {}'.format(t+1, minV))