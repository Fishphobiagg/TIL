# 집합의 표현
import sys

sys.setrecursionlimit(100000)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x
for i in range(M):
    command, A, B = map(int, input().split())
    if command:
        if find_parent(A) == find_parent(B):
            print('YES')
        else:
            print('NO')
    else:
        if A==B:
            continue
        union(A,B)

print(parent)