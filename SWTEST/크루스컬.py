# import sys
# sys.stdin = open('크루스컬.txt', 'r')

# 1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
# 2. 가중치가 가장 낮은 간선부터 선택하면서 트리 증가시킴
# 3. 사이클이 존재하면 다음으로 가중치가 낮은 간선을 선택한다.
# 4. n-1개의 간선이 선택될 때까지 두 번째 과정을 반복한다.

def Find_Set(a):
    # 값이 다르면 연결된 부분을 찾으러 간다.
    # 순회되지 않게 하기 위함
    if p[a] != a:
        p[a] = Find_Set(p[a])
    return p[a]


def Union(a, b):
    # 집합의 크기 비교
    if rank[a] < rank[b]:
        p[a] = b
    else:
        # 방문확인...?
        p[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    G = []  # 간선 정보, (시작 노드, 끝 노드, 가중치)
    p = [x for x in range(V+1)]  # 상호배타 집합 생성(연결된 노드로 이어준다.)
    rank = [0] * (V+1)
    for e in range(E):
        G.append(list(map(int, input().split())))

    G.sort(key=lambda x: x[2])  # 가중치 기준으로 정렬

    mst_cost = 0
    cnt = 0

    while cnt != V:
        if not G:
            break
        n1, n2, w = G.pop(0)  # 최소 가중치 간선 가져오기
        r_n1, r_n2 = Find_Set(n1), Find_Set(n2)
        if r_n1 != r_n2:
            Union(r_n1, r_n2)
            mst_cost += w
            cnt += 1

    print("#{0} {1}".format(t, mst_cost))