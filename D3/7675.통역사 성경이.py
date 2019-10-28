for t in range(int(input())):
    N = int(input())
    sentence = input().split()

    idx,case,jud = 0,[0]*N,True
    for i in range(len(sentence)):
        if sentence[i][-1] == '.' or sentence[i][-1] == '!' or sentence[i][-1] == '?':
            for j in range(len(sentence[i])-1):
                if j == 0:
                    if not 65 <= ord(sentence[i][j]) <= 90:
                        jud = False
                        break

                else:
                    if not 97 <= ord(sentence[i][j]) <= 122:
                        jud = False
                        break
            if jud == True:
                case[idx] += 1

            jud = True
            idx += 1

        else:
            for j in range(len(sentence[i])):
                if j == 0:
                    if not 65<=ord(sentence[i][j])<=90:
                        jud = False
                        break

                else:
                    if not 97<=ord(sentence[i][j])<=122:
                        jud = False
                        break

            if jud == True:
                case[idx] += 1

            jud = True

    print('#{} {}'.format(t+1, ' '.join(map(str, case))))