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

        elif command[idx] == 'D':
            x = int(command[idx + 1])
            y = int(command[idx + 2])
            for j in range(y):
                origin.pop(x)
            idx += 3

        elif command[idx] == 'A':
            y = int(command[idx+1])
            origin += command[idx+2 : idx+2+y]
            idx += 2 + y

    print(f'#{t+1} {" ".join(origin[:10])}')