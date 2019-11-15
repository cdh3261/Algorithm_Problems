for t in range(int(input())):
    N,M = map(int,input().split())
    time= sorted([int(input()) for i in range(N)])

    # nowTime = 0
    lastTime = time[0]
    for i in range(1,M):
        for j in range(N):
            if lastTime > time[j]:
                lastTime += time[j]
                time[j] = 2*time[j]
                break
            # nowTime = time[j]
            # lastTime = time[j]
            # time[j] = 2*time[j]
    print(lastTime)