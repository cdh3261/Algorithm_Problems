import sys,time
sys.stdin = open('요리사.txt', 'r')

for t in range(int(input())):
    start_time = time.time()

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minV = float('INF')
    for i in range(1,(1<<N)//2):
        first_man = []
        second_man = []
        for j in range(N):
            if i & (1<<j) != 0:
                first_man.append(j)
            else:
                second_man.append(j)
        if len(first_man)==N//2 and len(second_man)==N//2:
            firstV,secondV = 0,0
            for x in range(N//2):
                for y in range(x+1,N//2):
                    firstV += arr[first_man[x]][first_man[y]]+arr[first_man[y]][first_man[x]]
                    secondV += arr[second_man[x]][second_man[y]]+arr[second_man[y]][second_man[x]]
            if minV > abs(firstV-secondV):
                minV = abs(firstV-secondV)
    print('#{} {} 시간: %.4fsec'.format(t+1, minV) %(time.time()-start_time))