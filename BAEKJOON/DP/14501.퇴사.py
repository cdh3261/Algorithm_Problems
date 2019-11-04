N = int(input())
Ti,Pi = [0]*(N+1),[0]*(N+1)
for i in range(1,N+1):
    a,b = map(int,input().split())
    Ti[i],Pi[i] = a,b
dp = [0]*(N+2)
for i in range(1,N+2):
    for j in range(1,i):
        if j+Ti[j] == i:
            dp[i] = max(dp[i], Pi[j]+dp[j])
        else:
            dp[i] = max(dp[i],dp[j])
print(dp[-1])