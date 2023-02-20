# 숨바꼭질

from collections import deque


N, K = map(int, input().split())

arr = [0 for i in range(200001)]

Q = deque([N])

while Q:
    c = Q.popleft()
    check_list = []
    if c+1 <= 100000:
        check_list.append(c+1)
    if c*2 <= 200000:
        check_list.append(c*2)
    if c-1 >= 0:
        check_list.append(c-1)
    for i in check_list:
        if i == N:
            continue
        if not arr[i]:
            Q.append(i)
            arr[i] = arr[c] + 1
        elif arr[i] > arr[c] + 1:
            arr[i] = arr[c] + 1
print(arr[K])