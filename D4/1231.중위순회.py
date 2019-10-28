def inorder(n, last):
    if n<=last:
        inorder(n*2, last)
        print(tree[n], end='')
        inorder(n*2+1, last)

for t in range(10):
    N = int(input())
    tree = [0]*(N+1)

    for i in range(N):
        node = list(input().split())
        tree[i+1] = node[1]
    print('#{}'.format(t+1), end=' ')
    inorder(1, N)
    print()