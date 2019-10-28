# def f(n,s,d,m,m3): # n월, s : n-1월까지 사용 금액
#     global minV,p
#     if minV < s:
#         return
#     if n >= 13: # 10월이나 11월에도 3개월권을 끊을 수 있으므로..
#         if minV > s:
#             minV = s
#
#     else: # 1에서 12월 사이면
#         f(n+1, s+d*table[n], d, m, m3) # n월에 1일권 구입
#
#         f(n+1, s+m, d, m, m3) # n월에 1개월권 구입
#
#         f(n+3, s+m3, d, m, m3) # n월에 3개월권 구입
#
#
#
# for t in range(int(input())):
#     d, m, m3, y = map(int, input().split())
#     table = [0] + list(map(int, input().split()))
#     minV = y
#
#     f(1,0,d,m,m3) # 1월부터, 1월 이전 이용금액 0원
#     print('#{} {}'.format(t+1, minV))
#     print(p)

# 백트레킹
# def f(n, s):  # n월, s : n-1월까지 사용 금액
#     global minV, d, m, m3
#
#     if n >= 13:  # 10월이나 11월에도 3개월권을 끊을 수 있으므로..
#         if minV > s:
#             minV = s
#     elif minV < s:  # 중간에 minV보다 커지면 아웃
#         return
#     else:  # 1에서 12월 사이면
#         f(n + 1, s + d * table[n])  # n월에 1일권 구입
#         f(n + 1, s + m)  # n월에 1개월권 구입
#         f(n + 3, s + m3)  # n월에 3개월권 구입
#
#
# for t in range(int(input())):
#     d, m, m3, y = map(int, input().split())
#     table = [0] + list(map(int, input().split()))
#     minV = y
#
#     f(1, 0)  # 1월부터, 1월 이전 이용금액 0원
#     print('#{} {}'.format(t + 1, minV))

# DP 쓴것
T = int(input())
for t in range(1, T+1):
    d, m1, m3, y = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        if i < 3:
            dp[i] = dp[i-1] + min(d*month[i], m1)
        else:
            dp[i] = min((dp[i - 1] + min(d * month[i], m1)), dp[i-3] + m3)
    result = dp[-1]
    if y < dp[-1]:
        result = y
    print("#{} {}".format(t, result))