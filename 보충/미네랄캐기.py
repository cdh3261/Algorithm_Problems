import sys,time
sys.stdin = open('미네랄캐기','r')

def f(n,k,s,z,cnt):
    global maxV

    if cnt < 0 or z+s < maxV:
        return

    if n == k:
        maxV = max(maxV,s)
        return

    f(n+1,k,s+DE[n][1],z-DE[n][1],cnt-DE[n][0])
    f(n+1,k,s,z-DE[n][1],cnt)


for t in range(int(input())):
    starttime = time.time()
    N ,M ,C = map(int ,input().split())
    # 최초 충전 C

    arr = [list(map(int ,input().split())) for i in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                robot_I = i
                robot_J = j
                break

    DE = [[(abs(robot_I-i)+abs(robot_J-j))*2, arr[i][j]] for i in range(N) for j in range(M) if arr[i][j] > 1 and (abs(robot_I-i)+abs(robot_J-j))*2 <= C]

    maxV = 0
    ss = 0
    Lth = len(DE)
    for i in range(Lth):
        ss += DE[i][1]
    f(0,Lth,0,ss,C)

    # 비트연산자 -> 느림(비트는 일단 모든 경우의 수를 다 만들어서 느리다.)
    # for i in range(1<<Lth):
    #     s = 0
    #     Energy = C
    #     for j in range(Lth):
    #         if i & (1<<j) != 0:
    #             Energy -= DE[j][0]
    #             if Energy < 0 :
    #                 break
    #             s += DE[j][1]
    #     if Energy >= 0:
    #         maxV = max(maxV,s)

    print('답: {}   시간: %.4f sec 걸림'.format(maxV) %(time.time()-starttime))