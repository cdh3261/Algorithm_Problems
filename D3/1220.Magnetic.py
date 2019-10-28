#######    N극    #######

#######    S극    #######

for t in range(1, 11):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(n)]
    col = []
    for i in range(n):
        a = []
        for j in range(n):
            if arr[j][i] != 0:
                a.append(arr[j][i])
        col.append(a)

    cnt = 0
    for i in range(n):
        for j in range(len(col[i])):
            if j != 0 and col[i][j] == 2 and col[i][j - 1] != 2:
                cnt += 1
    print(f'#{t} {cnt}')