import sys
sys.stdin = open('점심식사시간.txt', 'r')

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
        one_distance, two_distance = [], []
        for j in range(Nth):
            if i & (1 << j) != 0:
                one_distance.append(abs(people[j][0]-exit[0][0]) + abs(people[j][1]-exit[0][1]))
            else:
                two_distance.append(abs(people[j][0]-exit[1][0]) + abs(people[j][1]-exit[1][1]))

        one_distance.sort()
        two_distance.sort()

        one_res = []
        for j in range(len(one_distance)):
            if j > 2:
                if one_distance[j] - one_distance[j-3] >= exit[0][2]:
                    one_res.append(one_distance[j]+1)
                else:
                    one_res.append(one_distance[j-3]+1 + exit[0][2])
            else:
                one_res.append(one_distance[j]+1)
        if one_res:
            one_res[-1] += exit[0][2]
        else:
            one_res.append(0)

        two_res = []
        for j in range(len(two_distance)):
            if j > 2:
                if two_distance[j] - two_distance[j-3] >= exit[1][2]:
                    two_res.append(two_distance[j]+1)
                else:
                    two_res.append(two_distance[j-3]+1 + exit[1][2])
            else:
                two_res.append(two_distance[j]+1)
        if two_res:
            two_res[-1] += exit[1][2]
        else:
            two_res.append(0)

        if minV > max(one_res[-1],two_res[-1]):
            minV = max(one_res[-1],two_res[-1])

    print('#{} {}'.format(t+1, minV))