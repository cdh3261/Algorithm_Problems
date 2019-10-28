for t in range(int(input())):
    N,M,K = map(int, input().split())
    people = list(map(int, input().split())) # 각각의 사람들이 오는 시간
    jud = True
    if 0 in people:
        jud = False
    else:
        num = max(people) # 오는 사람의 최고 시간까지만 보면된다.

        # M의 배수칸마다 K가 있다.(그 전에 남은 빵은 추가된다.)
        res = [0] * (num+1)
        for i in range(1, num+1):

            if i % M == 0: # 배수 부분에서는
                if i in people:
                    res[i] = res[i-1] + K - people.count(i) # 해당초에 오는 사람수를 빼야한다.
                    if res[i] < 0:
                        jud = False
                        break
                else:
                    res[i] = res[i-1] + K

            else:   # 배수가 아닌 부분
                if i in people:
                    res[i] = res[i-1] - people.count(i)
                    if res[i] < 0:
                        jud = False
                        break
                else:
                    res[i] = res[i-1]
    if jud:
        print('#{} Possible'.format(t+1))
    else:
        print('#{} Impossible'.format(t + 1))