# 상하좌우 -> 1,2,3,4
# 최대 5번 이동

def f(case):
    global arr,maxV
    # print(case)
    # case = [1,4,1,3,1]
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
        elif case[i]==3:
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
                    # print(case)
                    maxV = arr_copy[a][b]


def npr(n,k,c):
    global pre

    if p[n] == c:
        return

    if n == k:

        print(p)
        f(p)
        return

    for m in range(4):
        if used[n] == 0 and pre != m+1:
            used[n] = 1
            p[n] = m+1
            pre = m+1
            npr(n+1,k,m+1)
            # pre = 0
            used[n] = 0


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
p = [0]*5
used = [0]*5
pre = 0
maxV = 0
npr(0,5,-1)

print(maxV)