for t in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int,input().split())))[::-1]

    if N%2 == 0:
        left,right = [0]*(N//2),[0]*(N//2 -1)
    else:
        left,right = [0]*(N//2), [0]*(N//2)
    for i in range(1,N):
        if i%2 != 0:
            left[i//2] = arr[i]
        else:
            right[(i-1)//2] = arr[i]
    final = [arr[0]]+left+right[::-1]

    maxV = 0
    for i in range(N):
        if i == N-1:
            maxV = max(maxV,abs(final[i]-final[0]))
        else:
            maxV = max(maxV,abs(final[i]-final[i+1]))
    print('#{} {}'.format(t+1, maxV))