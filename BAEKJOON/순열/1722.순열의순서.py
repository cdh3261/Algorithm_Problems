N = int(input())
# a가 1이면 m를 입력받음, a가 2이면 순열을 받음
a = list(map(int, input().split()))

res = [0]*N
# 1이면 m번째 순열을 찾아라
if a[0] == 1:
    m = a[1]
    for i in range(1,N+1):
        res[i-1] = (m%i) +1
    print(res)
else:
    d = a[1:]