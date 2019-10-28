for t in range(int(input())):
    D,A,B,F = map(int, input().split())
    r = D/(A+B) * F
    print('#{} '.format(t+1) + '%.10f'%r)