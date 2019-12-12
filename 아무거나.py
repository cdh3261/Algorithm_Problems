def s(arr):
    global maxV

    A,B,C,D = 0,0,0,0
    A_direction,A_idx = 3,0
    B_direction,B_idx = 3,0
    C_direction,C_idx = 3,0
    D_direction,D_idx = 3,0

    for hole,going in arr:
        if hole == 1:
            A_idx += going
            # 같은 위치에 있을 때 return
            if (A_direction == B_direction and A_idx == B_idx) or (A_direction == C_direction and A_idx == C_idx) or (A_direction == D_direction and A_idx == D_idx):
                return

            # 도착 index를 넘어갈 때
            if A_idx >= len(points[A_direction]):
                # A += 40
                A_idx = 100
                continue

            # print(A_direction,A_idx)
            A += points[A_direction][A_idx]
            if A_direction == 3 and A_idx == 5:
                A_direction = 0
            elif A_direction == 3 and A_idx == 10:
                A_direction = 1
            elif A_direction == 3 and A_idx == 15:
                A_direction = 2

        elif hole == 2:
            B_idx += going
            if (B_direction == A_direction and B_idx == A_idx) or (B_direction == C_direction and B_idx == C_idx) or (B_direction == D_direction and B_idx == D_idx):
                return
            if B_idx >= len(points[B_direction]):
                # B += 40
                B_idx = 101
                continue
            B += points[B_direction][B_idx]
            if B_direction == 3 and B_idx == 5:
                B_direction = 0
            elif B_direction == 3 and B_idx == 10:
                B_direction = 1
            elif B_direction == 3 and B_idx == 15:
                B_direction = 2

        elif hole == 3:
            C_idx += going
            if (C_direction == B_direction and C_idx == B_idx) or (A_direction == C_direction and A_idx == C_idx) or (C_direction == D_direction and C_idx == D_idx):
                return
            if C_idx >= len(points[C_direction]):
                # C += 40
                C_idx = 102
                continue
            C += points[C_direction][C_idx]
            if C_direction == 3 and C_idx == 5:
                C_direction = 0
            elif C_direction == 3 and C_idx == 10:
                C_direction = 1
            elif C_direction == 3 and C_idx == 15:
                C_direction = 2

        else:
            D_idx += going
            if (D_direction == B_direction and D_idx == B_idx) or (D_direction == C_direction and D_idx == C_idx) or (A_direction == D_direction and A_idx == D_idx):
                return
            if D_idx >= len(points[D_direction]):
                # D += 40
                D_idx = 103
                continue
            D += points[D_direction][D_idx]
            if D_direction == 3 and D_idx == 5:
                D_direction = 0
            elif D_direction == 3 and D_idx == 10:
                D_direction = 1
            elif D_direction == 3 and D_idx == 15:
                D_direction = 2

    if A+B+C+D > maxV:
        # print('A_direction:{} A_idx:{} A:{}'.format(A_direction,A_idx,A))
        # print('B_direction:{} B_idx:{} B:{}'.format(B_direction, B_idx, B))
        # print('C_direction:{} C_idx:{} C:{}'.format(C_direction, C_idx, C))
        # print('D_direction:{} D_idx:{} D:{}'.format(D_direction, D_idx, D))
        print(arr)
        maxV = A+B+C+D

def npr(n,k):

    if n==k:
        s(p[:])
        return

    for m in range(4):
        p[n] = [m+1,go[n]]
        npr(n+1,k)


points = [
    [0,2,4,6,8,10,13,16,19,25,30,35,40],
    [0,2,4,6,8,10,12,14,16,18,20,22,24,25,30,35,40],
    [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,28,27,26,25,30,35,40],
    [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
]
go = list(map(int,input().split()))
p = [0]*10
maxV = 0
npr(0,10)
print(maxV)