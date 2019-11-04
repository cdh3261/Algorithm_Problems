N = int(input())
arr = list(map(int,input().split()))

M = int(input())
test = [list(map(int,input().split())) for i in range(M)]

last = []
cnt = 0
for i in range(M):
    jud = False
    j = 0
    while j < N:
        if arr == test[i]:
            jud = True
            break
        arr = arr[1:]+[arr[0]]
        j += 1

    if jud == True:
        cnt += 1
        last.append(test[i])
    else:
        re = test[i][:]
        for x in range(N):
            if test[i][x] == 1:
                test[i][x] = 3
            elif test[i][x] == 2:
                test[i][x] = 4
            elif test[i][x] == 3:
                test[i][x] = 1
            else:
                test[i][x] = 2
        test[i] = test[i][::-1]
        l = 0
        while l < N:
            if arr == test[i]:
                jud = True
                break
            arr = arr[1:]+[arr[0]]
            l += 1

        if jud == True:
            cnt += 1
            last.append(re)
print(cnt)
for i in range(cnt):
    print(' '.join(map(str, last[i])))
