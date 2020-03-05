# 시작: 19시 11분 // 끝: 20시 50분 ;;;;;;

def f(n,k):
    global minV

    if n == k:
        arrCopy = [arr[_][:] for _ in range(N)]
        redBall = RedBall[:]
        blueBall = BlueBall[:]
        cnt = 0
        for i in res:
            cnt += 1
            # 오른쪽 일때
            if i == 1:
                # 파랑공이 오른쪽에 있을 경우, 파랑 공을 먼저 움직인다.
                if redBall[0] == blueBall[0] and redBall[1] < blueBall[1]-1:
                    while 1:
                        if arrCopy[blueBall[0]][blueBall[1]+1] == '.':
                            arrCopy[blueBall[0]][blueBall[1]+1],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                            blueBall[1] += 1
                        elif arrCopy[blueBall[0]][blueBall[1]+1] == 'O':
                            return
                        else:
                            if arrCopy[redBall[0]][redBall[1]+1] == '.':
                                arrCopy[redBall[0]][redBall[1]+1],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                                redBall[1] += 1
                            elif arrCopy[redBall[0]][redBall[1]+1] == 'O':
                                return cnt
                            else:
                                break
                else:
                    while 1:
                        if arrCopy[redBall[0]][redBall[1]+1] == '.':
                            arrCopy[redBall[0]][redBall[1]+1],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                            redBall[1] += 1
                        elif arrCopy[redBall[0]][redBall[1]+1] == 'O':
                            arrCopy[redBall[0]][redBall[1]] = '.'
                            while 1:
                                if arrCopy[blueBall[0]][blueBall[1]+1] == '.':
                                    arrCopy[blueBall[0]][blueBall[1]+1],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                    blueBall[1] += 1
                                elif arrCopy[blueBall[0]][blueBall[1]+1] == 'O':
                                    return
                                else:
                                    return cnt
                        else:
                            if arrCopy[blueBall[0]][blueBall[1]+1] == '.':
                                arrCopy[blueBall[0]][blueBall[1]+1],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                blueBall[1] += 1
                            elif arrCopy[blueBall[0]][blueBall[1]+1] == 'O':
                                return
                            else:
                                break

            # 왼쪽
            elif i == 2:
                if redBall[0] == blueBall[0] and redBall[1] > blueBall[1]:
                    while 1:
                        if arrCopy[blueBall[0]][blueBall[1]-1] == '.':
                            arrCopy[blueBall[0]][blueBall[1]-1],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                            blueBall[1] -= 1
                        elif arrCopy[blueBall[0]][blueBall[1]-1] == 'O':
                            return
                        else:
                            if arrCopy[redBall[0]][redBall[1]-1] == '.':
                                arrCopy[redBall[0]][redBall[1]-1],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                                redBall[1] -= 1
                            elif arrCopy[redBall[0]][redBall[1]-1] == 'O':
                                return cnt
                            else:
                                break
                else:
                    while 1:
                        if arrCopy[redBall[0]][redBall[1]-1] == '.':
                            arrCopy[redBall[0]][redBall[1]-1],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                            redBall[1] -= 1
                        elif arrCopy[redBall[0]][redBall[1]-1] == 'O':
                            arrCopy[redBall[0]][redBall[1]] = '.'
                            while 1:
                                if arrCopy[blueBall[0]][blueBall[1]-1] == '.':
                                    arrCopy[blueBall[0]][blueBall[1]-1],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                    blueBall[1] -= 1
                                elif arrCopy[blueBall[0]][blueBall[1]-1] == 'O':
                                    return
                                else:
                                    return cnt
                        else:
                            if arrCopy[blueBall[0]][blueBall[1]-1] == '.':
                                arrCopy[blueBall[0]][blueBall[1]-1],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                blueBall[1] -= 1
                            elif arrCopy[blueBall[0]][blueBall[1]-1] == 'O':
                                return
                            else:
                                break

            # 위쪽
            elif i == 3:
                if redBall[0] > blueBall[0] and redBall[1] == blueBall[1]:
                    while 1:
                        if arrCopy[blueBall[0]-1][blueBall[1]] == '.':
                            arrCopy[blueBall[0]-1][blueBall[1]],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                            blueBall[0] -= 1
                        elif arrCopy[blueBall[0]-1][blueBall[1]] == 'O':
                            return
                        else:
                            if arrCopy[redBall[0]-1][redBall[1]] == '.':
                                arrCopy[redBall[0]-1][redBall[1]],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                                redBall[0] -= 1
                            elif arrCopy[redBall[0]-1][redBall[1]] == 'O':
                                return cnt
                            else:
                                break
                else:
                    while 1:
                        if arrCopy[redBall[0]-1][redBall[1]] == '.':
                            arrCopy[redBall[0]-1][redBall[1]],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                            redBall[0] -= 1
                        elif arrCopy[redBall[0]-1][redBall[1]] == 'O':
                            arrCopy[redBall[0]][redBall[1]] = '.'
                            while 1:
                                if arrCopy[blueBall[0]-1][blueBall[1]] == '.':
                                    arrCopy[blueBall[0]-1][blueBall[1]],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                    blueBall[0] -= 1
                                elif arrCopy[blueBall[0]-1][blueBall[1]] == 'O':
                                    return
                                else:
                                    return cnt
                        else:
                            if arrCopy[blueBall[0]-1][blueBall[1]] == '.':
                                arrCopy[blueBall[0]-1][blueBall[1]],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                blueBall[0] -= 1
                            elif arrCopy[blueBall[0]-1][blueBall[1]] == 'O':
                                return
                            else:
                                break

            # 아래
            else:
                if redBall[0] < blueBall[0] and redBall[1] == blueBall[1]:
                    while 1:
                        if arrCopy[blueBall[0]+1][blueBall[1]] == '.':
                            arrCopy[blueBall[0]+1][blueBall[1]],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                            blueBall[0] += 1
                        elif arrCopy[blueBall[0]+1][blueBall[1]] == 'O':
                            return
                        else:
                            if arrCopy[redBall[0]+1][redBall[1]] == '.':
                                arrCopy[redBall[0]+1][redBall[1]],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                                redBall[0] += 1
                            elif arrCopy[redBall[0]+1][redBall[1]] == 'O':
                                return cnt
                            else:
                                break
                else:
                    while 1:
                        if arrCopy[redBall[0]+1][redBall[1]] == '.':
                            arrCopy[redBall[0]+1][redBall[1]],arrCopy[redBall[0]][redBall[1]] = 'R','.'
                            redBall[0] += 1
                        elif arrCopy[redBall[0]+1][redBall[1]] == 'O':
                            arrCopy[redBall[0]][redBall[1]] = '.'
                            while 1:
                                if arrCopy[blueBall[0]+1][blueBall[1]] == '.':
                                    arrCopy[blueBall[0]+1][blueBall[1]],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                    blueBall[0] += 1
                                elif arrCopy[blueBall[0]+1][blueBall[1]] == 'O':
                                    return
                                else:
                                    return cnt
                        else:
                            if arrCopy[blueBall[0]+1][blueBall[1]] == '.':
                                arrCopy[blueBall[0]+1][blueBall[1]],arrCopy[blueBall[0]][blueBall[1]] = 'B','.'
                                blueBall[0] += 1
                            elif arrCopy[blueBall[0]+1][blueBall[1]] == 'O':
                                return
                            else:
                                break

        return

    for m in range(4):
        res[n] = m+1
        if n != 0 and res[n-1] == res[n]:
            pass
        else:
            r = f(n+1,k)

            if r != None:
                if minV > r:
                    minV = r
                # return r


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            RedBall = [i,j]
        elif arr[i][j] == 'B':
            BlueBall = [i,j]
#1,2,3,4 방향 순열로 .. but 앞에 똑같은 방향 x
res = [0,0,0,0,0,0,0,0,0,0]
minV = 11
f(0,10)
if minV == 11:
    print(-1)
else:
    print(minV)