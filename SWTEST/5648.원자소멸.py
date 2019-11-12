def f():
    global arr,N

    cnt = N
    s = 0
    while 1:
        z = 0
        while z!= cnt:
            if arr[z][2]==0:
                if arr[z][0]+1 <= 2000:
                    arr[z][0],arr[z][1],arr[z][2],arr[z][3]=arr[z][0]+1,arr[z][1],arr[z][2],arr[z][3]
                    z += 1
                else:
                    cnt -= 1
                    arr.pop(z)
            elif arr[z][2]==1:
                if arr[z][0]-1 > -2001:
                    arr[z][0],arr[z][1],arr[z][2],arr[z][3]=arr[z][0]-1,arr[z][1],arr[z][2],arr[z][3]
                    z += 1
                else:
                    cnt -= 1
                    arr.pop(z)
            elif arr[z][2]==2:
                if arr[z][1]-1 >= -2000:
                    arr[z][0],arr[z][1],arr[z][2],arr[z][3]=arr[z][0],arr[z][1]-1,arr[z][2],arr[z][3]
                    z += 1
                else:
                    cnt -= 1
                    arr.pop(z)
            elif arr[z][2]==3:
                if arr[z][1]+1 < 2001:
                    arr[z][0],arr[z][1],arr[z][2],arr[z][3]=arr[z][0],arr[z][1]+1,arr[z][2],arr[z][3]
                    z += 1
                else:
                    cnt -= 1
                    arr.pop(z)
            if cnt <= 1:
                return s

        x,y = 0,1

        while x!=cnt:
            jud = False
            while y!=cnt:
                # 같은 좌표에 있으면
                if arr[x][0] == arr[y][0] and arr[x][1]==arr[y][1]:
                    s += arr[y][3]
                    arr.pop(y)
                    cnt -= 1
                    jud = True
                else:
                    y+=1
            if jud==True:
                s += arr[x][3]
                arr.pop(x)
                y -= 1
                cnt -= 1
                if cnt <= 1:
                    return s
                jud=False
            else:
                x+=1
                y=x+1

        if cnt <= 1:
            return s

for t in range(int(input())):
    N = int(input())
    arr = []
    for i in range(N):
        x,y,d,e=map(int, input().split())
        arr.append([y*2,x*2,d,e])

    print('#{} {}'.format(t+1, f()))