import sys,time
sys.stdin = open('백조.txt','r')
input = sys.stdin.readline
start=time.time()

def enQ(a):
    global water, rear
    rear = (rear + 1) % (R*C)
    water[rear] = a

def deQ():
    global water,front
    front = (front + 1) % (R*C)
    return water[front]


def f():
    global distance,water,front,maxV

    while rear != front:
        i, j = deQ()
        for m in range(4):
            ni=i+di[m]
            nj=j+dj[m]
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] == 'X':
                    if distance[ni][nj] == 0:
                        distance[ni][nj] = distance[i][j]+1
                        if distance[ni][nj]>maxV:
                            maxV = distance[ni][nj]
                        enQ([ni,nj])

                    elif distance[ni][nj] > distance[i][j]+1:
                        distance[ni][nj] = distance[i][j]+1
                        enQ([ni,nj])



def check(i,j,V):
    global visited,M

    visited[i][j]=1
    q = []
    q.append([i,j])
    while q:
        i,j=q.pop(0)
        for k in range(4):
            ni=i+di[k]
            nj=j+dj[k]
            if 0<=ni<R and 0<=nj<C:
                if arr[ni][nj] == 'L':
                    return M
                if arr[ni][nj] <= V and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append([ni,nj])
                    if M<distance[ni][nj]:
                        M=distance[ni][nj]



di=[0,1,0,-1]
dj=[1,0,-1,0]

R,C=map(int,input().split())
arr = [list(input().strip()) for _ in range(R)]

water = [0]*(R*C)
monster = []
rear = front = -1
visited=[[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j]=='.':
            visited[i][j]=1
            for k in range(4):
                ni=i+di[k]
                nj=j+dj[k]
                if 0<=ni<R and 0<=nj<C:
                    if arr[ni][nj]=='X' and water[rear] != [i,j]:
                        enQ([i,j])
                        break

        elif arr[i][j]=='L':
            monster.append([i,j])

start_i,start_j = monster[0][0],monster[0][1]
end_i,end_j = monster[1][0], monster[1][1]

distance = [[0]*C for _ in range(R)]
maxV = 0
# distance[start_i][start_j]='L'
# distance[end_i][end_j]='L'

f()
M=-1
for i in range(maxV+1):
    if check(start_i,start_j,i) != -1:
        break
print(M)
for _ in range(R):
    print(distance[_])
print('%.4f sec' %(time.time()-start))