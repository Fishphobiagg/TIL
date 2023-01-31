from collections import deque
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    target_idx = M

    print_count = 0
    while len(importance) >= 0:
        if target_idx == 0 and max(importance) == importance[target_idx]:
            print(print_count+1)
            break
        elif target_idx == 0 and max(importance) != importance[target_idx]:
            importance.append(importance.popleft())
            target_idx = len(importance) - 1
            print_count += 1
        elif importance[0] < max(importance):
            importance.append(importance.popleft())
            target_idx -= 1
            print_count += 1

        