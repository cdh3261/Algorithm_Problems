for tc in range(int(input())):
    N = int(input())
    total = []
    for i in range(N):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi+1):
            total.append(j)
    P = int(input())
    res = [0]*5000
    for i in total:
        cnt = str(total.count(i))
        res[i] = cnt
    Cj_list = []
    for i in range(P):
        Cj = int(input())
        Cj_list.append(res[Cj])
    print(f"#{tc + 1} {' '.join(Cj_list)}")