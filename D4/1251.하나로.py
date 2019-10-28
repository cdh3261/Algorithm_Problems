import sys
sys.stdin = open('하나로.txt', 'r')

####### 25초 걸림##########

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
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

    distance = []
    for i in range(N):
        for j in range(i,N):
            dis = abs(xy_axis[i][0]-xy_axis[j][0])**2+abs(xy_axis[i][1]-xy_axis[j][1])**2
            if dis != 0:
                distance.append([dis, i+1, j+1])

    distance.sort()

    p = [i for i in range(N+1)]
    joint = [0]*(N+1)

    cnt = 0
    min_cost = 0

    while cnt < N-1:
        d, x, y = distance.pop(0)
        dx, dy = find(x), find(y)
        if dx != dy:
            union(dx, dy)
            cnt += 1
            min_cost += d

    print('#{} {}'.format(t+1, round(E*min_cost)))