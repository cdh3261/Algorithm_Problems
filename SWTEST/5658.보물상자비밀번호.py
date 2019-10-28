for t in range(int(input())):
    N,K=map(int,input().split())
    case = N//4

    arr = list(input())

    res = []
    start,end = 0,case
    for i in range(case):

        for j in range(4):
            if start > N:
                start -= N
            if end > N:
                end -= N

            if end>start:
                a=[''.join(arr[start:end]),int(''.join(arr[start:end]),16)]
                if not a in res:
                    res.append(a)
            else:
                b = [''.join(arr[start:]+arr[:end]),int(''.join(arr[start:]+arr[:end]),16)]
                if not b in res:
                    res.append(b)

            start += case
            end += case

        start += 1
        end += 1

    res.sort(key=lambda x: x[1])

    print('#{} {}'.format(t+1,res[-K][1]))