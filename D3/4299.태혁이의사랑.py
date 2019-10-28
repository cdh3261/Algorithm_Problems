#D일 H시 M분
for tc in range(int(input())):
    D,H,M = map(int, input().split())

    if (D ==11 and H == 11 and M >= 11) or (D ==11 and H > 11):
        #첫 날!
        hogoo = 60*(H-11) + (M-11)
        print(f'#{tc+1} {hogoo}')
    elif D > 11:
        #둘째날부터
        hogoo = 1440*(D-12) + (12+H)*60 + 49+M
        print(f'#{tc+1} {hogoo}')
    else :
        print(f'#{tc+1} -1')