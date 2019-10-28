import sys
sys.stdin = open('하나로한줄', 'r')


##################### 4초 걸림################

def enQueue(a):
    global rear, distance
    rear += 1
    distance[rear] = a


def deQueue():
    global front, distance
    front += 1
    return distance[front]


def find(a):
    # 재귀랑 별 차이없다.
    while p[a] != a:
        a = p[p[a]]
    return p[a]


def union(a, b):
    if joint[b] > joint[a]:
        p[a] = b
    else:
        p[b] = a
        if joint[b] == joint[a]:
            joint[a] += 1


a = list(map(float, input().split()))
idx = 1

for t in range(20):
    N = int(a[idx])
    idx += 1
    x_axis = a[idx:idx+N]
    idx += N
    y_axis = a[idx:idx+N]
    idx += N
    E = a[idx]
    idx += 1

    xy_axis = []
    for i in range(N):
        xy_axis.append([x_axis[i], y_axis[i]])

    distance = [0]*(N*(N-1)//2)
    front = rear = -1
    for i in range(N):
        for j in range(i,N):
            dis = abs(xy_axis[i][0]-xy_axis[j][0])**2+abs(xy_axis[i][1]-xy_axis[j][1])**2
            if dis != 0:
                enQueue([dis, i+1, j+1])

    distance.sort()

    p = [i for i in range(N+1)]
    joint = [0]*(N+1)

    cnt = 0
    min_cost = 0

    while cnt < N-1:
        d, x, y = deQueue()
        dx, dy = find(x), find(y)
        if dx != dy:
            union(dx, dy)
            cnt += 1
            min_cost += d

    print('#{} {}'.format(t+1, round(E*min_cost)))