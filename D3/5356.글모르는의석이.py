for tc in range(int(input())):

    start = [input() for i in range(5)]

    res = ''
    for j in range(max(len(start[0]),len(start[1]),len(start[2]),len(start[3]),len(start[4]))):
        for i in range(5):
            try:
                start[i][j]
                res += start[i][j]
            except IndexError:
                pass
    print(f'#{tc+1} {res}')