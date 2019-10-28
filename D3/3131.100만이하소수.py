B = 10 ** 6
sta = [False, False] + [True] * (B - 1)

for k in range(2, int(B ** 0.5) + 1):
    if sta[k]:
        sta[k * 2::k] = [False] * ((B - k) // k)

res = []
res += [str(x) for x in range(B + 1) if sta[x]]

print(' '.join(res))