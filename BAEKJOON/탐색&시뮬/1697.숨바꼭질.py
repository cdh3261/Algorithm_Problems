N,K = map(int, input().split())
inf = float('INF')
check = [inf]*100001
check[N] = 0

rear = front = -1
q = [0]*100001
rear += 1
q[rear]=N
while rear != front:
    front += 1
    i = q[front]
    if i == K:
        v = check[i]
        break
    for ni in (i-1),(i+1),(i*2):
        if 0<= ni <= 100000 and check[ni] == inf:
            if check[ni] > check[i]+1:
                check[ni] = check[i]+1
            rear += 1
            q[rear]=ni

print(v)