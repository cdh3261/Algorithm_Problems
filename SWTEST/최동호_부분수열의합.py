N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1,1<<N):
    s = 0
    for j in range(N):
        if i & (1<<j) != 0:
            s += nums[j]
    if s == S:
        cnt += 1
print(cnt)


