keypad = [[0],[0],['a','b','c'],['d','e','f'],['g','h','i'],
          ['j','k','l'],['m','n','o'],['p','q','r','s'],
          ['t','u','v'],['w','x','y','z']]
for t in range(int(input())):
    S,N = input().split()
    N = int(N)
    arr = input().split()
    cnt,i = 0,0
    for j in range(N):
        jud = True
        for k in arr[j]:
            if not k in keypad[int(S[i])]:
                jud = False
                break
            else:
                i += 1
        if jud == True:
            cnt += 1
        i = 0
    print('#{} {}'.format(t+1, cnt))