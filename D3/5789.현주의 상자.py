for t in range(int(input())):
    N, Q = map(int, input().split())
    nums = ['0' for i in range(1, N+1)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())

        #L부터 R까지 숫자를 i로 바꾸기
        for j in range(L-1, R):
            nums[j] = str(i)

    print(f'#{t+1} {" ".join(nums)}')