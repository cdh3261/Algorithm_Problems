la = []
tcc =int(input())
for tc in range(tcc):
    i = int(input())
    j = i
    numbers = list(map(int, input().split()))
    res = []
    for a in range(i):
        for b in range(a+1, j):
            mul = str(numbers[a] * numbers[b])
            if len(mul) > 1 and not '0' in mul:
                res.append(mul)
    re = [0]
    for y in range(len(res)):
        cd = True
        for z in range(1, len(res[y])):
            if int(res[y][z]) < int(res[y][z-1]):
                cd = False
                break
        if cd and int(res[y]) > re[-1]:
            re += [int(res[y])]
    if len(re) == 1:
        la.append(-1)
    else:
        la.append(re[-1])

for l in range(1,tcc+1):
    print(f'#{l} {la[l-1]}')