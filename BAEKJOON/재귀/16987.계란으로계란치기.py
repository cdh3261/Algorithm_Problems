def f(I,cnt,eggs):
    global maxV

    maxV = max(maxV, cnt)
    if I == N:
        return

    if eggs[I][0] > 0:
        for i in range(N):
            if eggs[i][0] > 0 and i != I:
                eggs[I][0] -= eggs[i][1]
                eggs[i][0] -= eggs[I][1]
                add = 0
                if eggs[I][0] <= 0:
                    add += 1
                if eggs[i][0] <= 0:
                    add += 1
                f(I+1,cnt+add,eggs)
                eggs[I][0] += eggs[i][1]
                eggs[i][0] += eggs[I][1]
    else:
        f(I+1,cnt,eggs)

N = int(input())
eggs = [list(map(int,input().split())) for i in range(N)]
maxV = 0
f(0,0,eggs)
print(maxV)