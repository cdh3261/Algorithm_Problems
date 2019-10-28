# 미완성

for tc in range(int(input())):
    total = []
    for N in range(int(input())):
        Ai, Bi = map(int, input().split())
        total.extend(range(Ai,Bi+1))

    res = []
    for P in range(int(input())):
        Cj = int(input())
        if Cj in total:
            res.append(str(total.count(Cj)))
        else:
            res.append('0')

    print(f'#{tc+1} {" ".join(res)}')