for t in range(10):
    N = int(input())    # 원본 암호문의 길이
    origin = input().split() # 원본 암호문
    cN = int(input()) # 명령어의 개수
    command = input().split() # 명령어

    idx = 0
    for i in range(cN):

        if command[idx] == 'I':
            x = int(command[idx+1])
            y = int(command[idx+2])
            for j in range(y):
                origin.insert(x+j, command[idx+3+j])
            idx += 3 + y

    print(f'#{t+1} {" ".join(origin[:10])}')