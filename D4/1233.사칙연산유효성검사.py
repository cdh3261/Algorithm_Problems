import sys
sys.stdin = open('유효성.txt', 'r')

for t in range(10):
    N = int(input())

    jud = True
    cal = [list(input().split()) for i in range(N)]

    for i in range(N):
        if len(cal[i]) == 4:
            if cal[i][1].isdigit():
                jud = False
                break
        else:
            if not cal[i][1].isdigit():
                jud = False
                break

    if jud:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))