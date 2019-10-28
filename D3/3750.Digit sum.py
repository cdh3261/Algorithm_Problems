def dsum(n):
    s = 0
    for i in n:
        s += int(i)

    if len(str(s)) == 1:
        return s
    else:
        return dsum(str(s))

test = int(input())
res = []
for tc in range(test):
    n = input()
    res.append(dsum(n))

for j in range(test):
    print(f'#{j+1} {res[j]}')