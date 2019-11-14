def f(n):
    global idx1, idx2_L, idx2_R, idx3_L, idx3_R, idx4, first_idx, second_idx, third_idx, forth_idx

    if first[idx1] != second[idx2_L]:
        if second[idx2_R] != third[idx3_L]:
            if third[idx3_R] != forth[idx4]:
                first_idx, idx1 = first_idx-n, idx1-n
                second_idx, idx2_R, idx2_L = second_idx+n, idx2_R+n, idx2_L+n
                third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
                forth_idx, idx4 = forth_idx+n, idx4+n
            else:
                first_idx, idx1 = first_idx-n, idx1-n
                second_idx, idx2_R, idx2_L = second_idx+n, idx2_R+n, idx2_L+n
                third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
        else:
            first_idx, idx1 = first_idx-n, idx1-n
            second_idx, idx2_R, idx2_L = second_idx+n, idx2_R+n, idx2_L+n
    else:
        first_idx, idx1 = first_idx-n, idx1-n


def t(n):
    global idx1, idx2_L, idx2_R, idx3_L, idx3_R, idx4, first_idx, second_idx, third_idx, forth_idx
    if first[idx1] != second[idx2_L]:
        first_idx, idx1 = first_idx+n, idx1+n

    if second[idx2_R] != third[idx3_L]:
        if third[idx3_R] != forth[idx4]:
            second_idx, idx2_L, idx2_R = second_idx-n, idx2_L-n, idx2_R-n
            third_idx, idx3_R, idx3_L = third_idx+n, idx3_R+n, idx3_L+n
            forth_idx, idx4 = forth_idx-n, idx4-n
        else:
            second_idx, idx2_L, idx2_R = second_idx-n, idx2_L-n, idx2_R-n
            third_idx, idx3_R, idx3_L = third_idx+n, idx3_R+n, idx3_L+n
    else:
        second_idx, idx2_L, idx2_R = second_idx-n, idx2_L-n, idx2_R-n


def th(n):
    global idx1, idx2_L, idx2_R, idx3_L, idx3_R, idx4, first_idx, second_idx, third_idx, forth_idx

    if third[idx3_R] != forth[idx4]:
        forth_idx, idx4 = forth_idx+n, idx4+n

    if third[idx3_L] != second[idx2_R]:
        if second[idx2_L] != first[idx1]:
            second_idx, idx2_L, idx2_R = second_idx+n, idx2_L+n, idx2_R+n
            third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
            first_idx, idx1 = first_idx-n, idx1-n
        else:
            second_idx, idx2_L, idx2_R = second_idx+n, idx2_L+n, idx2_R+n
            third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
    else:
        third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n


def fo(n):
    global idx1, idx2_L, idx2_R, idx3_L, idx3_R, idx4, first_idx, second_idx, third_idx, forth_idx
    if forth[idx4] != third[idx3_R]:
        if third[idx3_L] != second[idx2_R]:
            if second[idx2_L] != first[idx1]:
                first_idx, idx1 = first_idx-n, idx1-n
                second_idx, idx2_R, idx2_L = second_idx+n, idx2_R+n, idx2_L+n
                third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
                forth_idx, idx4 = forth_idx+n, idx4+n
            else:
                second_idx, idx2_R, idx2_L = second_idx+n, idx2_R+n, idx2_L+n
                third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
                forth_idx, idx4 = forth_idx+n, idx4+n
        else:
            third_idx, idx3_R, idx3_L = third_idx-n, idx3_R-n, idx3_L-n
            forth_idx, idx4 = forth_idx+n, idx4+n
    else:
        forth_idx, idx4 = forth_idx+n, idx4+n


for tc in range(int(input())):
    K = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    third = list(map(int, input().split()))
    forth = list(map(int, input().split()))
    Kth = [list(map(int, input().split())) for _ in range(K)]
    s = 0
    first_idx, second_idx, third_idx, forth_idx = 0, 0, 0, 0
    idx1, idx2_L, idx2_R, idx3_L, idx3_R, idx4 = 2, 6, 2, 6, 2, 6
    for i in range(K):
        if Kth[i][0] == 1:
            if Kth[i][1] == 1:
                f(1)
            else:
                f(-1)
        elif Kth[i][0] == 2:
            if Kth[i][1] == 1:
                t(1)
            else:
                t(-1)
        elif Kth[i][0] == 3:
            if Kth[i][1] == 1:
                th(1)
            else:
                th(-1)
        else:
            if Kth[i][1] == 1:
                fo(-1)
            else:
                fo(1)

        if first_idx == 8 or first_idx == -8:
            first_idx = 0
        if second_idx == 8 or second_idx == -8:
            second_idx = 0
        if third_idx == 8 or third_idx == -8:
            third_idx = 0
        if forth_idx == 8 or forth_idx == -8:
            forth_idx = 0
        if idx1 == 8 or idx1 == -8:
            idx1 = 0
        if idx2_L == 8 or idx2_L == -8:
            idx2_L = 0
        if idx2_R == 8 or idx2_R == -8:
            idx2_R = 0
        if idx3_R == 8 or idx3_R == -8:
            idx3_R = 0
        if idx3_L == 8 or idx3_L == -8:
            idx3_L = 0
        if idx4 == 8 or idx4 == -8:
            idx4 = 0

    if first[first_idx] == 1:
        s += 1
    if second[second_idx] == 1:
        s += 2
    if third[third_idx] == 1:
        s += 4
    if forth[forth_idx] == 1:
        s += 8

    print('#{} {}'.format(tc+1, s))