def f(s, e):
    global jud

    if s == e:
        jud = 1
        return
    else:
        if a1[s]:
            f(a1[s], e)
        if a2[s]:
            f(a2[s], e)
        return

for t in range(1, 11):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    a1 = [0]*100
    a2 = [0]*100
    jud = 0

    for i in range(m):
        if a1[arr[2*i]]:
            a2[arr[2*i]] = arr[2*i+1]
        else:
            a1[arr[2*i]] = arr[2*i+1]
    f(0,99)
    print('#{} {}'.format(t, jud))