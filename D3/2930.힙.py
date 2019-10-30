for t in range(int(input())):
    N = int(input())
    case = [list(map(int,input().split())) for i in range(N)]

    print('#{}'.format(t+1),end=' ')
    res = [0]*N
    rear,front = -1,-1
    for arr in case:
        if arr[0] == 1:
            if front!=rear:
                jud=False
                for i in range(N):
                    if res[i] != 0 and arr[1]>res[i]:
                        res[i],res[i+1:]=arr[1],res[i:]
                        rear += 1
                        jud=True
                        break
                if jud==False:
                    rear += 1
                    res[rear]=arr[1]

            else:
                rear += 1
                res[rear]=arr[1]


        else:
            if front!=rear:
                front += 1
                print(res[front], end=' ')
            else:
                print(-1)