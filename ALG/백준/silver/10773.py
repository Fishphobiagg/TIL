# 제로
from collections import deque
K = int(input())

stack = []

for i in range(K):
    A = int(input())
    if A == 0:
        del stack[-1]
    else:
        stack.append(A)

print(sum(stack))