#D를 포함하고 A~B 사이의 소수

def prime(n):
    cnt = 0

    #n이 2이하 또는 2의 배수이면 소수가 아니다.
    if n <= 2:
        return 0
    if n % 2 == 0:
        return 0

    #정수의 제곱근까지만 판단해줘도 소수인지 아닌지 알 수 있다.
    squ = int(n ** 0.5)
    for i in range(3, squ + 1, 2):
        if n % i == 0:
            return 0
    if str(D) in str(n):
        cnt += 1
        return cnt
    else:
        return 0


for tc in range(int(input())):
    D, A, B = map(int, input().split())
    s = 0
    for n in range(A, B + 1):
        s += prime(n)
    print(f'#{tc+1} {s}')




######시간 짧은 답
# B = 10 ** 6
# sta = [False, False] + [True] * (B - 1)
# 
# for k in range(2, int(B ** 0.5) + 1):
#     if sta[k]:
#         sta[k * 2::k] = [False] * ((B - k) // k)
# 
# for t in range(int(input())):
#     res = []
#     D, A, B = map(int, input().split())
#     sD = str(D)
# 
#     res += [x for x in range(A, B + 1) if sta[x] and sD in str(x)]
# 
#     print('#{} {}'.format(t + 1, len(res)))