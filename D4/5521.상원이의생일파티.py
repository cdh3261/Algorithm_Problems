for t in range(int(input())):
    N, M = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(M)]

    V = [0]*(N+1)
    cnt = 0
    for i in range(M):
        x, y= friends[i][0], friends[i][1]
        if x == 1 and V[y] == 0:
            cnt += 1
            V[y] = 1
        elif x != 1:
            for j in range(M):
                w,z = friends[j][0],friends[j][1]
                if w == 1 and z == x and V[y] == 0:
                    cnt += 1
                    V[y] = 1
                    break
                if w == 1 and z == y and V[x] == 0:
                    cnt += 1
                    V[x] = 1
                    break
        if cnt == N:
            break

    print('#{} {}'.format(t+1, cnt))