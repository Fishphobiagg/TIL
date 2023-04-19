# 교수님 살려주세요 과제가 너무 많아요
import sys
import heapq
input = sys.stdin.readline

assignment = []
Q = []
for i in range(int(input())):
    A, B = map(int, input().split())
    assignment.append((A, B))

assignment.sort()

for x, i in assignment:
    heapq.heappush(Q, i)
    if len(Q) == x+1:
        heapq.heappop(Q)

print(sum(Q))