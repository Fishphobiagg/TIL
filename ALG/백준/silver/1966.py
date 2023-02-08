from collections import deque
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    target_idx = M
    