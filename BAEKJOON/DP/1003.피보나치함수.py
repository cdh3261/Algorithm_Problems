f = [[0]]*41
f[0] = [1,0]
f[1] = [0,1]
for i in range(2,41):
    f[i] = [f[i-1][0]+f[i-2][0], f[i-1][1]+f[i-2][1]]

for t in range(int(input())):
    N = int(input())
    print(f[N][0], f[N][1])