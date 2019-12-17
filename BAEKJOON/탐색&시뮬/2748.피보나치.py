f = [0]*91
f[1] = 1
for i in range(2,91):
    f[i] = f[i-1]+f[i-2]
print(f[int(input())])