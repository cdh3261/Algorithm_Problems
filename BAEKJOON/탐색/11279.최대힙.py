t = int(input())
heap = [0]*(t+1)
idx = 0
for i in range(1,t+1):
    N = int(input())

    if N != 0:
        idx += 1
        heap[idx] = N
        change_idx = idx
        while change_idx//2 > 0 and heap[change_idx] > heap[change_idx//2]:
            heap[change_idx//2], heap[change_idx] = heap[change_idx], heap[change_idx//2]
            change_idx = change_idx//2
    # 0이 들어오면 최대힙 출력과 팝
    else:
        # 마지막 노드와 첫 번째 노드 교환
        heap[1], heap[-1] = heap[-1], heap[1]
        maxV = heap.pop()
        print(maxV)
        k = 1
        left = k*2
        right = k*2+1

        while 1:
            if left < len(heap) and right < len(heap):
                if heap[left] > heap[right]:
                    heap[k], heap[left] = heap[left], heap[k]
                    k = left
                elif heap[left] < heap[right]:
                    heap[k], heap[right] = heap[right], heap[k]
                    k = right
                else:
                    break
            elif left < len(heap) and heap[left] > heap[k]:
                heap[k], heap[left] = heap[left], heap[k]
                k = left
            else:
                break