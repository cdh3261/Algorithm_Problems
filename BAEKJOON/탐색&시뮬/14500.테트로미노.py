# 19시 시작 // 20시 5분 끝

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 5가지 모양.
# 1-1) 일자모양
total = 0
for i in range(N):
    for j in range(M-3):
        s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
        if total < s:
            total = s
# 1-2)
for i in range(N-3):
    for j in range(M):
        s = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
        if total < s:
            total = s

# 2) 네모모양
# 0<=ni<=M-2 , 0<=nj<=N-2
for i in range(N-1):
    for j in range(M-1):
        s = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
        if total < s:
            total = s

# 3-1,2) L모양
for i in range(N-2):
    for j in range(M-1):
        s = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
        ss = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
        sss = arr[i+2][j] + arr[i+2][j+1] + arr[i+1][j+1] + arr[i][j+1]
        ssss = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j]
        sssss = max(s,ss,sss,ssss)
        if total < sssss:
            total = sssss
# 3-3,4) L모양
for i in range(N-1):
    for j in range(M-2):
        s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j]
        ss = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
        sss = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
        ssss = arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2] + arr[i][j+2]
        sssss = max(s,ss,sss,ssss)
        if total < sssss:
            total = sssss

# 4-1) z모양
for i in range(N-2):
    for j in range(M-1):
        s = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
        ss = arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j] + arr[i+2][j]
        if total < s:
            total = s
        if total < ss:
            total = ss
# 4-2) z모양
for i in range(N-1):
    for j in range(M-2):
        s = arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2]
        ss = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
        if total < s:
            total = s
        if total < ss:
            total = ss

# 5-1) ㅜ모양
for i in range(N-1):
    for j in range(M-2):
        s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
        ss = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
        if total < s:
            total = s
        if total < ss:
            total = ss
# 5-2)
for i in range(N-2):
    for j in range(M-1):
        s = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1]
        ss = arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
        if total < s:
            total = s
        if total < ss:
            total = ss

print(total)