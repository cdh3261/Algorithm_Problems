def f(i,j,k,A,B):
    while 1:
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<A and 0<=nj<B:
            if arr[ni][nj] == -1:
                return
            if arr[ni][nj] != 0:
                if arr[i][j] == -1:
                    arr[ni][nj] = 0
                else:
                    arr[i][j],arr[ni][nj] = arr[ni][nj],0

            i,j = ni,nj

        elif ni == -1:
            k = 1
        elif nj == B:
            k = 2
        elif ni == A:
            k = 3
        elif nj == -1:
            k = 0


di,dj = [-1,0,1,0],[0,1,0,-1]

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

# 확산되는 양 => x/5
# 남은 양 => x - (x/5)*확산갯수

robot = [[i,0,0] for i in range(N) if arr[i][0] == -1]
robot[1][2] = 2

f(robot[0][0],robot[0][1],robot[0][2],robot[1][0],M)
f(robot[1][0],robot[1][1],robot[1][2],robot[0][0],M)