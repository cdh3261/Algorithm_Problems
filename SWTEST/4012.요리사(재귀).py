import sys,time
sys.stdin = open('요리사.txt', 'r')

def ncr(n,k,cnt):
    global first_man, second_man, minV,c,case

    if c == case//2:
        return

    if cnt == N//2:
        c += 1
        second_man = list(nums-set(first_man))
        FV, SV = 0, 0
        for i in range(N//2):
            for j in range(i+1,N//2):
                FV += arr[first_man[i]][first_man[j]]+arr[first_man[j]][first_man[i]]
                SV += arr[second_man[i]][second_man[j]]+arr[second_man[j]][second_man[i]]
        minV = min(minV, abs(FV-SV))
        return

    if n == k :
        return

    else:
        first_man[cnt] = n
        ncr(n+1,k,cnt+1)
        ncr(n+1,k,cnt)

for t in range(int(input())):
    start_time = time.time()
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = set(i for i in range(N))
    first_man = [0]*(N//2)
    minV = float('INF')

    case = 1
    ca = 1
    for i in range(N,N//2,-1):
        case = case*i
        ca = ca*(i-N//2)
    case = case//ca

    c =0
    ncr(0,N,0)

    print('#{} {} 시간: %.4fsec'.format(t + 1, minV) % (time.time() - start_time))