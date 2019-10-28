# 하이픈

for tc in range(int(input())):
    start = ''
    start += input()
    hi = int(input())

    a, b, c = map(int, input().split())
    res = start[:a] + '-' + start[a:]
    res = res[:b] + '-' + res[b:]
    res = res[:c] + '-' + res[c:]
    print(f'#{tc+1} {res}')