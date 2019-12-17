def f(case):
    global arr,maxV
    arr_copy = [arr[_][:] for _ in range(N)]
    for i in range(5):
        # 위로
        if case[i] == 1:
            for y in range(N):
                for x in range(N-1):
                    if arr_copy[x][y] == 0:
                        z = x+1
                        while z != N:
                            if arr_copy[z][y] != 0:
                                arr_copy[x][y],arr_copy[z][y] = arr_copy[z][y],0
                                break
                            z += 1

            for y in range(N):
                for x in range(N-1):
                    if arr_copy[x][y] != 0:
                        for z in range(x+1,N):
                            if arr_copy[z][y] == arr_copy[x][y]:
                                arr_copy[x][y],arr_copy[z][y] = arr_copy[x][y]*2,0
                                break
                            elif arr_copy[z][y] != 0:
                                break

            for y in range(N):
                for x in range(N-1):
                    if arr_copy[x][y] == 0:
                        z = x+1
                        while z != N:
                            if arr_copy[z][y] != 0:
                                arr_copy[x][y],arr_copy[z][y] = arr_copy[z][y],0
                                break
                            z += 1
        # 하
        elif case[i] == 2:
            for y in range(N):
                for x in range(N-1,0,-1):
                    if arr_copy[x][y] == 0:
                        z = x-1
                        while z != -1:
                            if arr_copy[z][y] != 0:
                                arr_copy[x][y],arr_copy[z][y] = arr_copy[z][y],0
                                break
                            z -= 1

            for y in range(N):
                for x in range(N-1,0,-1):
                    if arr_copy[x][y] != 0:
                        for z in range(x-1,-1,-1):
                            if arr_copy[z][y] == arr_copy[x][y]:
                                arr_copy[x][y],arr_copy[z][y] = arr_copy[x][y]*2,0
                                break
                            elif arr_copy[z][y] != 0:
                                break

            for y in range(N):
                for x in range(N-1,0,-1):
                    if arr_copy[x][y] == 0:
                        z = x-1
                        while z != -1:
                            if arr_copy[z][y] != 0:
                                arr_copy[x][y],arr_copy[z][y] = arr_copy[z][y],0
                                break
                            z -= 1
        # 좌
        elif case[i] == 3:
            for x in range(N):
                for y in range(N-1):
                    if arr_copy[x][y] == 0:
                        z = y+1
                        while z != N:
                            if arr_copy[x][z] != 0:
                                arr_copy[x][y],arr_copy[x][z] = arr_copy[x][z],0
                                break
                            z += 1

            for x in range(N):
                for y in range(N-1):
                    if arr_copy[x][y] != 0:
                        for z in range(y+1,N):
                            if arr_copy[x][z] == arr_copy[x][y]:
                                arr_copy[x][y],arr_copy[x][z] = arr_copy[x][y]*2,0
                                break
                            elif arr_copy[x][z] != 0:
                                break

            for x in range(N):
                for y in range(N-1):
                    if arr_copy[x][y] == 0:
                        z = y+1
                        while z != N:
                            if arr_copy[x][z] != 0:
                                arr_copy[x][y],arr_copy[x][z] = arr_copy[x][z],0
                                break
                            z += 1

        # 우
        else:
            for x in range(N):
                for y in range(N-1,0,-1):
                    if arr_copy[x][y] == 0:
                        z = y-1
                        while z != -1:
                            if arr_copy[x][z] != 0:
                                arr_copy[x][y],arr_copy[x][z] = arr_copy[x][z],0
                                break
                            z -= 1

            for x in range(N):
                for y in range(N-1,0,-1):
                    if arr_copy[x][y] != 0:
                        for z in range(y-1,-1,-1):
                            if arr_copy[x][y] == arr_copy[x][z]:
                                arr_copy[x][y],arr_copy[x][z] = arr_copy[x][y]*2,0
                                break
                            elif arr_copy[x][z] != 0:
                                break

            for x in range(N):
                for y in range(N-1,0,-1):
                    if arr_copy[x][y] == 0:
                        z = y-1
                        while z != -1:
                            if arr_copy[x][z] != 0:
                                arr_copy[x][y],arr_copy[x][z] = arr_copy[x][z],0
                                break
                            z -= 1

        for a in range(N):
            for b in range(N):
                if maxV < arr_copy[a][b]:
                    maxV = arr_copy[a][b]


def npr(n,k):
    if maxV == s:
        return

    if n == k:
        if p[4] == p[3]:
            return
        f(p)
        return~
    if n > 1 and p[n-1] == p[n-2]:
        return
    for m in range(4):
        if used[n] == 0:
            used[n] = 1
            p[n] = m+1
            npr(n+1,k)
            used[n] = 0


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]
p = [0]*5
used = [0]*5
maxV = 0
npr(0,5)
print(maxV)