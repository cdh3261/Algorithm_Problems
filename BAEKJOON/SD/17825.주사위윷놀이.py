def f(n,k):
    global maxV,p

    if n == k:
        idx = [0,0,0,0]
        check = [0]*33
        total_score = 0
        for i in range(10):
            next_idx = points[idx[p[i]]][arr[i]]
            if check[next_idx] == 1 and next_idx != 32:
                return
            check[idx[p[i]]] = 0
            check[next_idx] = 1
            idx[p[i]] = next_idx
            get_score = points[next_idx][0]
            total_score += get_score
        if maxV < total_score:
            maxV = total_score
        return

    for m in range(4):
        p[n] = m
        f(n+1,k)

arr = list(map(int,input().split()))
p = [0]*10

maxV = 0

points = [
    [0,1,2,3,4,5],
    [2,2,3,4,5,9],
    [4,3,4,5,9,10],
    [6,4,5,9,10,11],
    [8,5,9,10,11,12],
    [10,6,7,8,20,29],
    [13,7,8,20,29,30],
    [16,8,20,29,30,31],
    [19,20,29,30,31,32],
    [12,10,11,12,13,14],
    [14,11,12,13,14,15],
    [16,12,13,14,15,16],
    [18,13,14,15,16,17],
    [20,18,19,20,29,30],
    [22,15,16,17,24,25],
    [24,16,17,24,25,26],
    [26,17,24,25,26,27],
    [28,24,25,26,27,28],
    [22,19,20,29,30,31],
    [24,20,29,30,31,32],
    [25,29,30,31,32,32],
    [26,20,29,30,31,32],
    [27,21,20,29,30,31],
    [28,22,21,20,29,30],
    [30,23,22,21,20,29],
    [32,26,27,28,31,32],
    [34,27,28,31,32,32],
    [36,28,31,32,32,32],
    [38,31,32,32,32,32],
    [30,30,31,32,32,32],
    [35,31,32,32,32,32],
    [40,32,32,32,32,32],
    [0,32,32,32,32,32]
]
f(0,10)
print(maxV)