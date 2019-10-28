X = int(input())
dp = [0]*(X+1)
if X != 1:
    dp[2] = 1

for i in range(3,X+1):
    if i % 3 == 0:
        if dp[i//3]>dp[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i//3] + 1
    elif i % 2 == 0:
        if dp[i//2]>dp[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i//2] + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[-1])