N = int(input())
nums = [int(input()) for i in range(N)]
if N == 1:
    print(nums[0])
elif N == 2:
    print(sum(nums))
else:
    dp = [0]*N
    dp[0] = nums[0]
    dp[1] = nums[0]+nums[1]
    for i in range(2,N):
        dp[i] = max(nums[i]+nums[i-1]+dp[i-3],nums[i]+dp[i-2],dp[i-1])
    print(dp[-1])