def switch(arr, arr_copy, cnt):
    if arr[0] != 0:
        if arr_copy[arr[0][0]][arr[0][1]] == 1:
            arr_copy[arr[0][0]][arr[0][1]] = 0
            cnt += 1
        arr[0] = 0
    return cnt


def dis(k, arr, i, j):
    if D >= k:
        if arr[0] == 0:
            arr[0] = [i, j, k]
        else:
            if arr[0][2] > k:
                arr[0] = [i, j, k]
            elif arr[0][2] == k and arr[0][1] > j:
                arr[0] = [i, j, k]


def shoot(location):
    arr_copy = [arr[i][:] for i in range(N)]

    total_cnt = 0
    for z in range(N):
        first_D, second_D, third_D = [0], [0], [0]
        for i in range(N-1, -1, -1):
            for j in range(M):
                if arr_copy[i][j] == 1:
                    k1 = abs(i-location[0][0])+abs(j-location[0][1])
                    k2 = abs(i-location[1][0])+abs(j-location[1][1])
                    k3 = abs(i-location[2][0])+abs(j-location[2][1])
                    dis(k1, first_D, i, j)
                    dis(k2, second_D, i, j)
                    dis(k3, third_D, i, j)

        total_cnt += switch(first_D, arr_copy, 0)+switch(second_D, arr_copy, 0)+switch(third_D, arr_copy, 0)

        for i in range(N-1, 0, -1):
            arr_copy[i] = arr_copy[i-1][:]
        arr_copy[0] = [0]*M

    return total_cnt


def f(n, k, cnt, location):
    global maxV

    if cnt == 3:
        V = shoot(location)
        if maxV < V:
            maxV = V
        return

    if n == k:
        return
    f(n+1, k, cnt+1, location+[[N, n]])
    f(n+1, k, cnt, location)


N, M, D = map(int, input().split())
arr, maxV = [list(map(int, input().split())) for i in range(N)], 0
f(0, M, 0, [])
print(maxV)