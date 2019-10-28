import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(TC):
    N,D = map(int, input().split()) # 부먹 왕국의 도시 수 N, 이동 제한 거리 D(1 ≤ D ≤ N)
    maps = [1] + list(map(int, input().split())) + [1] # 지도 정보


    cnt = 0
    i = 0
    while i < N: # d-1거리까지 보면서 1이 중간에 있으면 그 1을 다시 본다.
        try:
            maps[i+D]
            if not 1 in maps[i+1:i+D+1]:
                maps[i+D] = 1
                cnt += 1
                i += D
            else:
                i += 1

        except IndexError:
            break

    print('#{} {}'.format(t+1, cnt))