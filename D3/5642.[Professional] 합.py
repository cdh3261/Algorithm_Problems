# TC = int(input())
# for t in range(TC):
#     N = int(input()) # 정수의 개수
#     nums = list(map(int, input().split())) # N개의 정수들
#
#     maxN = max(nums)
#     if maxN < 0:    # maxN이 음수면 모든 정수들이 음수이므로 더할 필요가 없다.
#         print('#{} {}'.format(t+1, maxN))
#
#     else:
#         m = 0 # 최대값 저장
#         s = 0 # 값 저장
#         for i in range(N):
#             if nums[i] >= 0:
#                 for j in range(i, N):
#                     s += nums[j]
#                     if s > m:
#                         m = s
#                 s = 0
#
#         print('#{} {}'.format(t+1, m))


TC = int(input())
for t in range(TC):
    N = int(input()) # 정수의 개수
    nums = list(map(int, input().split())) # N개의 정수들

    maxN = max(nums)
    if maxN < 0:    # maxN이 음수면 모든 정수들이 음수이므로 더할 필요가 없다.
        print('#{} {}'.format(t+1, maxN))

    else:
        m = 0
        s = 0
        for i in range(N):
            num = nums[i]
            if i == N-1 and num > 0:
                s += num
                if s > m:
                    m = s
            elif i == N-1 and num <= 0:
                pass
            elif num < 0 and s + num <= 0:
                if s > m:
                    m = s
                s = 0
            elif num >= 0:
                s += num
                if s > m:
                    m = s
            else:
                s += num

        print('#{} {}'.format(t+1, m))