# N = int(input())
# arr = list(map(int,input().split()))
#
# idx = 0
# res = [0]*N
# ju = False
# for i in range(N-1):
#     for j in range(i+1,N):
#         if arr[i] < arr[j]:
#             ju = True
#             res[idx] = arr[j]
#             idx += 1
#             break
#     if ju == False:
#         res[idx] = -1
#         idx += 1
#     ju = False
# res[-1] = -1
# print(*res)

N = int(input())
arr = list(map(int,input().split()))

ju = False
for i in range(N-1):
    for j in range(i+1,N):
        if arr[i] < arr[j]:
            ju = True
            print(arr[j], end=' ')
            break
    if ju == False:
        print(-1, end=' ')
    ju = False
print(-1)