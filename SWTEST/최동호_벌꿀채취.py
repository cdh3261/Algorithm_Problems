def value(M,C,jud):
    global bee

    maxV = 0
    # M = 3이라 생각하면
    for x in range(1 << M):  # 1<<M을 2**M-1 로 줄 수 있다.
        s = 0  # 부분 집합의 합
        ss = 0
        for y in range(M):  # 0,1,2번 비트
            if x & (1 << y) != 0 and s + jud[y] <= C:  # i의 j번 비트가 1이고, 합계가 제한량 이하면
                s += jud[y]
                ss += jud[y] * jud[y]  # 채취한 벌꿀의 가치
        if maxV < ss:
            maxV = ss
    return maxV

for t in range(int(input())):
    N, M, C = map(int, input().split()) # NxN행렬, 한 일꾼의 벌통의 수 M(연속)가로, 한 일꾼의 최대양 C

    bee = [list(map(int, input().split())) for i in range(N)]
    # M개의 원소에서 1개 이상, 최대 M개를 고르는 방법.

    m = []
    for i in range(N):
        mm = 0
        for j in range(N-M+1):
            if bee[i][j] > C:
                pass
            else:
                jud1 = bee[i][j:j+M]
                a = value(M, C, jud1)
                if mm < a:
                    mm = a
        m.append(mm)

    m1 = m.pop(m.index(max(m)))
    m2 = max(m)
    print('#{} {}'.format(t+1, m1+m2))