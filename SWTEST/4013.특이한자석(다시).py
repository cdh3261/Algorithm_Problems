import sys
sys.stdin = open('자석.txt','r')

def f(i,l,n):
    ri = arr[i][2]
    le = arr[i][6]

    if l==1:
        arr[i] = [arr[i][7]]+arr[i][:7]
    else:
        arr[i] = arr[i][1:]+[arr[i][0]]

    if i+1 < 4 and arr[i+1][6] != ri and (n or n == 2):
        f(i+1,-1*l,2)
    if i-1 >= 0 and arr[i-1][2] != le and (n or n == 3):
        f(i-1,-1*l,3)

for t in range(int(input())):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    for i in range(k):
        n, l = map(int, input().split())
        f(n-1, l, 1)
    print('#{} {}'.format(t+1, arr[0][0]+arr[1][0]*2+arr[2][0]*4+arr[3][0]*8))