N= int(input())
a = list(map(int, input().split()))

up = [i for i in range(1,N+1)]
down = [i for i in range(N,0,-1)]

if N==1 or a == down:
    print(-1)
elif a==up:
    a[-1],a[-2] = a[-2],a[-1]
    print(' '.join(map(str, a)))
else:
    jud = False
    for i in range(N-1):
        if a[-i-2] < a[-i-1]:
            j = 1
            while 1:
                if a[-i-2] < a[-j]:
                    a[-i-2], a[-j] = a[-j], a[-i-2]
                    a = a[:-i-1]+sorted(a[-i-1:])
                    jud = True
                    break
                else:
                    j += 1
            if jud == True:
                break
    print(' '.join(map(str, a)))