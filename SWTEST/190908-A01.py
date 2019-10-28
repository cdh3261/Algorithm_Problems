def npr(n,k,N):
    global village, used, p

    if n == k:
        first.append(p[:])
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i+1
                npr(n+1,k,N)
                used[i] = 0

TC = int(input())
for t in range(TC):

    # N 마을수
    N = int(input())

    # 각 마을의 연결지점
    village = [list(map(int, input().split())) for i in range(N)]

    # 각 마을의 인원수
    people = list(map(int, input().split()))

    # 최소값과 첫번째 지역구(두번째 지역구는 첫번째 지역구를 알고 전체에서 빼주면 된다.)
    minV = 1000000
    first = []

    # 두 지역구를 나누는데 한 지역구에 1개이상 N-1개이하 마을이 있어야 한다.
    # 순열로 각 마을을 저장한다.
    for z in range(1, N):
        used = [0]*N
        p = [0]*z
        npr(0,z,N)

    # 첫번째 지역구의 마을들의 마을번호를 fi에 넣는다.
    for i in range(len(first)):
        fi = first[i]
        se = []
        jud = False

        # N은 0~N-1번이므로 마을 번호를 1~N으로 잡기위해 범위를 1~N+1로 해준다.
        # 그 마을 번호가 없는 마을이 두번째 지역구로 들어간다.
        for j in range(1,N+1):
            if not j in fi:
                se.append(j)

        # 첫번째 지역구의 마을들이 연결되어 있는지 판단
        for j in range(len(fi)-1):
            if village[fi[j]-1][fi[j+1]-1] == 1:
                jud = True
            else:
                jud = False
                break

        # 첫번째 지역구의 마을들이 연결되어 있으면 두번째 지역구를 판단
        if jud == True:
            for j in range(len(se)-1):
                if village[se[j]-1][se[j+1]-1] == 1:
                    jud = True
                else:
                    jud = False
                    break

            # 두 지역구 모두 연결되어 있으면 각 마을들에 대한 인원을 더하고
            # 두 지역구의 차이를 계산한다.
            if jud == True:
                first_sum = 0
                second_sum = 0
                for x in fi:
                    first_sum += people[x-1]
                for x in se:
                    second_sum += people[x-1]
                if minV > abs(first_sum-second_sum):
                    minV = abs(first_sum-second_sum)
    print(minV)