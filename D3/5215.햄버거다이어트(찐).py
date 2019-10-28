for t in range(int(input())):

    # L => 최대 칼로리
    N, L = map(int, input().split())
    case = [list(map(int, input().split())) for i in range(N)]

    #부분집합을 비트연산자로 생각하기.
    #case[][0]들이 점수, case[][1]들이 칼로리
    res = []
    for i in range(1<<N):
        score = 0
        calories = 0
        for j in range(N):
            if i & (1<<j):
                score += case[j][0]
                calories += case[j][1]
                # if calories > L:
                #     break
        if calories <= L:
            res.append(score)

    print('#{} {}'.format(t+1, max(res)))