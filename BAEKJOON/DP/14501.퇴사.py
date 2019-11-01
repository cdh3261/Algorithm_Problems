N = int(input())
Ti,Pi = [0]*(N+1),[0]*(N+1)

for i in range(1,N+1):
    a,b = map(int,input().split())
    Ti[i],Pi[i] = a,b

dp = [[[0,0] for j in range(N+1)] for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if j>=i:
            if j-1 + Ti[j-1] >= N+1 :
                dp[i][j] = [dp[i][j-1][0],dp[i][j-1][1]]
            elif dp[i][j-1][0] <= j:
                dp[i][j][1] = dp[i][j-1][1]+Pi[j]
                dp[i][j][0] = j+Ti[j]
            else:

                dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1]]
        # else:
        #     dp[i][j] = [dp[i-1][j][0],dp[i-1][j][1]]
for i in range(1,N+1):
    print(dp[i])
maxV = 0
for i in range(1,N+1):
    maxV = max(maxV,dp[i][-1][1])
print(maxV)