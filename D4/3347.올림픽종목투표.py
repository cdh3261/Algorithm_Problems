for t in range(int(input())):
    N,M = map(int,input().split())
    A,B = list(map(int,input().split())),list(map(int,input().split()))
    C = [0]*N
    for i in range(M):
        for j in range(N):
            if A[j]<=B[i]:
                C[j] += 1
                break
    print('#{} {}'.format(t+1, C.index(max(C))+1))