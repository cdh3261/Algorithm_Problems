import sys
sys.stdin = open('혁진이.txt','r')

def f(i,j,k):
    global memory

    res.append([i,j,k,memory[0]])
    stack = []
    stack.append([i,j,k])
    while stack:
        i,j,k=stack.pop()
        if arr[i][j] == '@':
            return 'YES'
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<R and 0<=nj<C:
            if arr[ni][nj] == '@':
                return 'YES'

            if arr[ni][nj]=='<':
                k = 2
                i, j = ni, nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='>':
                k = 0
                i, j = ni, nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='^':
                k = 3
                i, j = ni, nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='v':
                k = 1
                i, j = ni, nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='_':
                if memory[0] == 0:
                    k = 0
                else:
                    k = 2
                i, j = ni, nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='|':
                if memory[0] == 0:
                    k = 1
                else:
                    k = 3
                i, j = ni, nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='?':
                i,j=ni,nj
                for k in range(4):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if 0<=ni<R and 0<=nj<C :
                        if arr[ni][nj]=='@':
                            return 'YES'

                        if arr[ni][nj]=='^':
                            if not [ni, nj, 3, memory[0]] in res:
                                res.append([ni,nj,3, memory[0]])
                                stack.append([ni,nj,3])
                        elif arr[ni][nj]=='<':
                            if not [ni, nj, 2, memory[0]] in res:
                                res.append([ni, nj, 2, memory[0]])
                                stack.append([ni, nj, 2])
                        elif arr[ni][nj] == '>':
                            if not [ni, nj, 0, memory[0]] in res:
                                res.append([ni, nj, 0, memory[0]])
                                stack.append([ni, nj, 0])
                        elif arr[ni][nj]=='v':
                            if not [ni, nj, 1, memory[0]] in res:
                                res.append([ni, nj, 1, memory[0]])
                                stack.append([ni, nj, 1])
                        elif arr[ni][nj]=='?' or arr[ni][nj]=='.':
                            if not [ni, nj, k, memory[0]] in res:
                                res.append([ni, nj, k, memory[0]])
                                stack.append([ni, nj, k])
                        elif arr[ni][nj]=='+':
                            if memory[0]==15:
                                memory[0]=0
                            else:
                                memory[0]+=1
                            if not [ni, nj, k, memory[0]] in res:
                                res.append([ni, nj, k, memory[0]])
                                stack.append([ni, nj, k])
                        elif arr[ni][nj]=='-':
                            if memory[0]==0:
                                memory[0]=15
                            else:
                                memory[0]-=1
                            if not [ni, nj, k, memory[0]] in res:
                                res.append([ni, nj, k, memory[0]])
                                stack.append([ni, nj, k])
                        elif arr[ni][nj]=='|':
                            if memory[0]==0:
                                k=1
                            else:
                                k=3
                            if not [ni, nj, k, memory[0]] in res:
                                res.append([ni, nj, k, memory[0]])
                                stack.append([ni, nj, k])
                        elif arr[ni][nj]=='_':
                            if memory[0]==0:
                                k=0
                            else:
                                k=2
                            if not [ni, nj, k, memory[0]] in res:
                                res.append([ni, nj, k, memory[0]])
                                stack.append([ni, nj, k])
                        elif arr[ni][nj].isdigit():
                            memory[0]=int(arr[ni][nj])
                            if not [ni, nj, k, memory[0]] in res:
                                res.append([ni, nj, k, memory[0]])
                                stack.append([ni, nj, k])

            elif arr[ni][nj]=='.':
                i,j = ni,nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='+':
                if memory[0]==15:
                    memory[0]=0
                else:
                    memory[0] += 1
                i,j = ni,nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            elif arr[ni][nj]=='-':
                if memory[0]==0:
                    memory[0]=15
                else:
                    memory[0] -= 1
                i,j = ni,nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
            else:
                memory[0]=int(arr[ni][nj])
                i,j = ni,nj
                if not [ni, nj, k,memory[0]] in res:
                    res.append([ni, nj, k, memory[0]])
                    stack.append([ni,nj,k])
        elif ni==R:
            ni=0
            stack.append([ni,nj,k])
        elif nj==C:
            nj=0
            stack.append([ni,nj,k])
        elif ni==-1:
            ni=R-1
            stack.append([ni,nj,k])
        elif nj==-1:
            nj=C-1
            stack.append([ni,nj,k])

    return 'NO'

di,dj=[0,1,0,-1],[1,0,-1,0]
for t in range(int(input())):
    R,C = map(int, input().split())

    arr=[list(input()) for _ in range(R)]
    c = 0
    for i in range(R):
        if '@' in arr[i]:
            c+=1
    if c == 0:
        print('#{} NO'.format(t+1))
    else:
        res=[]
        k = 0
        memory = [0]
        if arr[0][0] == '@':
            print('#{} YES'.format(t+1))
        elif arr[0][0] == '?':
            jud=False
            for l in range(4):
                i = di[l]
                j = dj[l]
                if i==R:
                    i=0
                elif j==C:
                    j=0
                elif i==-1:
                    i=R-1
                elif j==-1:
                    j=C-1

                if f(i, j, l) == 'YES':
                    jud = True

            if jud==True:
                print('#{} YES'.format(t+1))
            else:
                print('#{} NO'.format(t+1))
        else:
            if arr[0][0].isdigit():
                memory = [int(arr[0][0])]
            elif arr[0][0] == '+':
                memory = [1]
            elif arr[0][0] == '-':
                memory = [15]
            elif arr[0][0] == '<':
                k = 2
            elif arr[0][0] == '^':
                k = 3
            elif arr[0][0] == 'v':
                k = 1
            elif arr[0][0] == '|':
                k = 1
            else:
                memory = [0]
            print('#{} {}'.format(t+1, f(0,0,k)))
