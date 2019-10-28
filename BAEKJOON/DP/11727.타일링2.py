N = int(input())
r,a,b = 1,1,3
if N == 1:
    r = 1
elif N == 2:
    r = 3
else:
    for i in range(3,N+1):
        r = 2*a+b
        a,b = b,r
print(r%10007)