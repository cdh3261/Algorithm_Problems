for t in range(int(input())):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt,i = 0,0
    while i != N:
        cnt += i+1
        if arr[i]>M:
            arr[i] -= M
        elif arr[i]==M:
            i += 1
        else:
            if i == N-1:
                break
            else:
                MM = M
                while i != N:
                    if MM-arr[i]>0:
                        MM -= arr[i]
                        if i != N-1:
                            cnt += 1
                        i += 1
                    else:
                        arr[i] -= MM
                        break
    print('#%d %d' %(t+1,cnt*2))