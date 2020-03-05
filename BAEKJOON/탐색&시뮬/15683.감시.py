#시작 7시 41분

# 첫번째 cctv
def f(go):
    global total

    cnt = total
    for m in range(4):
        



N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
total = N*M

one,one_ = [],0
two,two_ = [],0
thr,thr_ = [],0
four,four_ = [],0
five,five_ = [],0
loc = []
# 6 벽
for i in range(N):
    for j in range(M):
        if arr[i][j] == 6:
            total -= 1
        elif arr[i][j] == 1:
            total -= 1
            one.append([i,j])
            one_ += 1
        elif arr[i][j] == 2:
            total -= 1
            two.append([i,j])
            two_ += 1
        elif arr[i][j] == 3:
            total -= 1
            thr.append([i,j])
            thr_ += 1
        elif arr[i][j] == 4:
            total -= 1
            four.append([i,j])
            four_ += 1
        elif arr[i][j] == 5:
            total -= 1
            five.append([i,j])
            five_ += 1
