# n 사용한 종이수, s 남은 1의 개수
def f(n,s):
    global minV

    if s == 0:
        if minV > n:
            minV = n
    elif minV == 4:
        return
    elif sum(paper) == 0:
        return
    else:
        for i in range(10):
            for j in range(10):
                if m[i][j] == 1 and visited[i][j] == 0: # 왼쪽 모서리로 가정
                    # 남아있는 종이를 크기 k로 덮어본다.

                        # i,j를 왼쪽 위 모서리로 덮을 수 있으면
                            f(n+1,s-k*k)


                    return



m = [list(map(int, input().split())) for i in range(10)]
visited = [[0]*10 for _ in range(10)]
minV = 26
paper = [0,5,5,5,5,5]
cnt = 0
s = 0
for i in range(10):
    s += m[i].count(1)

f(0,s)
if minV == 26:
    minV = -1
print(minV)
