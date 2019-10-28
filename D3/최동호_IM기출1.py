TC = int(input())
for t in range(TC):
    N = int(input()) # 방의 개수
    rooms = list(map(int, input().split())) # 각 방들의 원하는 불빛

    cnt = 0 # 카운트
    for i in range(N):
        if rooms[i] == 1:
            cnt += 1
            n = i
            while n < N:    # 불빛이 켜져 있으면 배수들의 방 불빛을 바꾼다.
                if rooms[n] == 0:
                    rooms[n] = 1
                else:
                    rooms[n] = 0
                n += (i+1) # 배수 증가

    print('#{} {}'.format(t+1, cnt))