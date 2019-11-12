import sys
sys.stdin = open('점심식사시간.txt', 'r')

def f(res,distance,k):
    for j in range(len(distance)):
        if j > 2:
            if distance[j]-distance[j-3] >= exit[k][2]:
                res.append(distance[j]+1)
            else:
                res.append(distance[j-3]+1+exit[k][2])
        else:
            res.append(distance[j]+1)
    if res:
        res[-1] += exit[k][2]
    else:
        res.append(0)


for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('INF')

    people, exit = [], []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append([i, j])
            elif arr[i][j] != 0 and arr[i][j] != 1:
                exit.append([i, j, arr[i][j]])

    Nth = len(people)
    for i in range(1 << Nth):
        one_d, two_d = [], []
        for j in range(Nth):
            if i & (1 << j) != 0:
                one_d.append(abs(people[j][0]-exit[0][0]) + abs(people[j][1]-exit[0][1]))
            else:
                two_d.append(abs(people[j][0]-exit[1][0]) + abs(people[j][1]-exit[1][1]))

        one_d.sort()
        two_d.sort()

        one_res,two_res = [],[]
        f(one_res,one_d,0)
        f(two_res,two_d,1)

        minV = min(minV,max(one_res[-1],two_res[-1]))

    print('#{} {}'.format(t+1, minV))