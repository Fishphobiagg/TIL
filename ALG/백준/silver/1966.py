from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
<<<<<<< Updated upstream
    target_idx = M
    
=======
    count = 0
    while True:
        max_i = max(importance)
        c = importance.popleft()
        if M == -1:
            M = len(importance)
        if c == max_i and M == 0:
            count += 1
            print(count)
            break
        elif c == max_i:
            count += 1
            M -= 1
        else:
            importance.append(c)
            M -= 1
>>>>>>> Stashed changes
