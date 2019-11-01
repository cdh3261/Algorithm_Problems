for t in range(int(input())):
    string = input()
    N = len(string)

    if N % 2 == 1:
        M = N//2
    else:
        M = N//2 -1

    left,right,cnt = 0,-1,0
    i,j = 0,0
    while i != M+1 and j != -(M+2):
        if string[left+i] == string[right-j]:
            i += 1
            j += 1
        else:
            if string[left + i+1] == string[right - j]:
                i += 1
                cnt += 1
            elif string[left+i] == string[right - j -1]:
                j += 1
                cnt += 1
            else:
                cnt = 2

            if cnt == 2:
                break
    if cnt == 2:
        left, right, cnt = 0, -1, 0
        i, j = 0, 0
        while i != M+1 and j != -(M+2):
            if string[left+i] == string[right-j]:
                i += 1
                j += 1
            else:
                if string[left+i] == string[right-j-1]:
                    j += 1
                    cnt += 1
                elif string[left+i+1] == string[right-j]:
                    i += 1
                    cnt += 1

                else:
                    cnt = 2

                if cnt == 2:
                    break
    print(cnt)