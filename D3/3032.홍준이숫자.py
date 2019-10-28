for t in range(int(input())):
    A, B = map(int, input().split())

    if A > B: # 5 3
        n = B
        i = 1
        j = 0
        while 1:
            if n % B == 0 and (1 - n) % A == 0:
                break
            if n < A:
                i += 1
                n = B*i
            else:
                j += 1
                n = A*j
        x = (1-n)//A
        y = n//B

    elif B > A:
        n = A
        i = 1
        j = 0
        while 1:
            if n % A == 0 and (1 - n) % B == 0:
                break
            if n < B:
                i += 1
                n = A * i
            else:
                j += 1
                n = B * j
        y = (1 - n) // B
        x = n // A


    else:
        print('#{} -1'.format(t+1))
    print('#{} {} {}'.format(t+1, x, y))