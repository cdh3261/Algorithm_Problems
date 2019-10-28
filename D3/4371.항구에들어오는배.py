for t in range(int(input())):
    N = int(input())
    # 배수를 쉽게 구하기 위해 입력값에서 1씩을 다 뺀다.
    days = []
    for i in range(N):
        n = int(input())-1
        if n != 0: # 첫 날은 필요없다.
            days.append(n)

    # 배수를 삭제한다.
    i = 0
    while i < len(days)-1:
        n = days[i]
        j = i + 1
        while j < len(days):
            if days[j] % n == 0:
                days.pop(j)
            else:
                j += 1
        i += 1
    print('#{} {}'.format(t+1, len(days)))

# for t in range(int(input())):
#     N = int(input())
#     # 배수를 쉽게 구하기 위해 입력값에서 1씩을 다 뺀다.
#     days = [int(input()) - 1 for i in range(N)]
#     days.pop(0)  # 첫 날은 필요없다.
#
#     # 배수를 삭제한다.
#     i = 0
#     while i < len(days) - 1:
#         n = days[i]
#         j = i + 1
#         while j < len(days):
#             if days[j] % n == 0:
#                 days.pop(j)
#             else:
#                 j += 1
#         i += 1
#     print('#{} {}'.format(t + 1, len(days)))