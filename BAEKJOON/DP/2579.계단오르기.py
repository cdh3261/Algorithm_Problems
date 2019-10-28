N = int(input())
a = [0] + [int(input()) for i in range(N)]
dp = [0]*(N+1)
dp[1] = a[1]
dp[2] = a[1]+a[2]
dp[3] = max(a[1]+a[3],a[2]+a[3])
for i in range(4,N+1):
    dp[i] = max(a[i]+dp[i-2],a[i]+a[i-1]+dp[i-3])
print(dp[-1])