# 벽 또는 자시자신의 몸과 부딪히면 게임 끝
# 왼쪽 맨위.

def f(i,j):
    global arr,time

    k = 0
    tail = [[0, 0]]
    for ti in range(1,time+1):
        if X[ti] == 'L':#왼쪽90도
            k -= 1
            if k == -1:
                k = 3
        elif X[ti] == 'D': #오른쪽90도
            k += 1
            if k == 4:
                k = 0

        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] == 'A':
                arr[ni][nj] = 'X'
                tail.append([ni,nj])
            elif arr[ni][nj] == 0:
                a,b=tail.pop(0)
                arr[a][b] = 0
                arr[ni][nj] = 'X'
                # 꼬리 변경
                tail.append([ni,nj])
            elif arr[ni][nj] == 'X':
                return ti+1
            i,j = ni,nj
        else:
            return ti+1


di,dj=[0,1,0,-1],[1,0,-1,0]

N=int(input())
K=int(input())
arr = [[0]*N for _ in range(N)]
for i in range(K):
    a,b=map(int,input().split())
    arr[a][b] = 'A'
L=int(input())
X=[0]*10001
for i in range(L):
    a,b=map(str,input().split())
    time = int(a)
    X[int(a)]=b

arr[0][0]='X'
print(f(0,0))