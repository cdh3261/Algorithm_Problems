N = int(input())
nums = [0]+list(map(int, input().split()))
dp = [-1001]*(N+1)
for i in range(1,N+1):
    dp[i] = max(dp[i-1]+nums[i],nums[i])
print(max(dp))