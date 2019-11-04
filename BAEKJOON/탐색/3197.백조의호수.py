import sys,time
sys.stdin = open('백조.txt','r')
input = sys.stdin.readline
start=time.time()


def water1(i,j):
    global meet,arr,re,visited
    # visited = [[0] * C for _ in range(R)]
    # arr[i][j] = '.'
    q = [0]*(R*C)
    rear = front = -1
    rear += 1
    q[rear]=[i,j]
    re += 1
    monster1[re]=[i,j]
    while rear != front:
        front += 1
        i,j = q[front]
        visited[i][j] = 1
        for m in range(4):
            ni=i+di[m]
            nj=j+dj[m]
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] == '.' and visited[ni][nj]==0:
                    # arr[ni][nj] = 'X'
                    visited[ni][nj]=1
                    rear += 1
                    q[rear]=[ni,nj]
                    # re += 1
                    # monster1[re] = [ni,nj]
                elif arr[ni][nj] == 'L' and visited[ni][nj]==0:
                    return 0
                elif arr[ni][nj]=='X' and visited[ni][nj]==0:
                    visited[ni][nj]=1
                    re += 1
                    monster1[re]=[i,j]

def water2(i,j):
    global meet,arr,r,visited
    # visited = [[0] * C for _ in range(R)]
    # arr[i][j] = 'X'
    q = [0]*(R*C)
    rear = front = -1
    rear += 1
    q[rear]=[i,j]
    r += 1
    monster2[r]=[i,j]
    while rear != front:
        front +=1
        i,j = q[front]
        visited[i][j]=1
        for m in range(4):
            ni=i+di[m]
            nj=j+dj[m]
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] == '.' and visited[ni][nj]==0:
                    visited[ni][nj]=1
                    # arr[ni][nj] = 'X'
                    rear += 1
                    q[rear]=[ni,nj]
                    # r += 1
                    # monster2[r]=[ni,nj]
                elif arr[ni][nj] == 'L' and visited[ni][nj]==0:
                    return 0
                elif arr[ni][nj]=='X' and visited[ni][nj]==0:
                    visited[ni][nj]=1
                    r += 1
                    monster2[r]=[i,j]


# def case(i,j):




di=[0,1,0,-1]
dj=[1,0,-1,0]

R,C=map(int,input().split())
arr = [list(input().strip()) for _ in range(R)]

monster1 = [0]*(R*C)
re=-1
monster2 = [0]*(R*C)
r=-1

jud=False
c = 0
for i in range(R):
    for j in range(C):
        if arr[i][j]=='L':
            visited = [[0] * C for _ in range(R)]
            if c == 0:
                c = 1
                if water1(i,j) == 0:
                    jud=True
                    print(0)
                    print('%.4f sec 걸렸습니다.' % (time.time() - start))
                    break
            else:
                if water2(i,j) == 0:
                    jud=True
                    print(0)
                    print('%.4f sec 걸렸습니다.' % (time.time() - start))
                    break

    if jud==True:
        break

if jud==False:
    minV = float('INF')
    for i in range(re+1):
        for j in range(r+1):
            I,J=monster1[i][0],monster1[i][1]
            f_I,f_J=monster2[j][0],monster2[j][1]
            # case(i,j)
            dis = abs(monster1[i][0]-monster2[j][0])+abs(monster1[i][1]-monster2[j][1])
            dis = (dis+1)//2
            if minV>dis:
                minV=dis
                print('{},{}'.format([I,J],[f_I,f_J]))
            if minV == 1:
                break
        if minV == 1:
            break
    print(minV)
    print('%.4f sec 걸렸습니다.' %(time.time()-start))