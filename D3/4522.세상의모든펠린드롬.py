for t in range(int(input())):
    st = list(input())
    N,j = len(st),1
    for i in range(N//2):
        if st[i]=='*' or st[-i-1]=='*':
            break
        elif st[i] != st[-i-1]:
            j=0
            break
    print('#{} Exist'.format(t+1)) if j else print('#{} Not exist'.format(t+1))