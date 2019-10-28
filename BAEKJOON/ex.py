arr = [[1,2,3,4,5] for _ in range(5)]
#2~3 K


# if K == 0 : j-K ~ j+K
# 가운데가 아니면 i-K ~ i+K

for k in range(2,4):
    for i in range(5):
        for j in range(5):
            s = 0
            for z in range(k + 1):
                if z == 0:
                    s += sum(arr[i][j-z:j+z+1])
                else:
                    s += sum(arr[i-z][j-z:j+z+1])+sum(arr[i+z][j-z:j+z+1])