dp = [0]*90
dp[0],dp[1] = 1,1

for i in range(2,90):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[int(input())-1])