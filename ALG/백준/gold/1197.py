# 최소 스패닝 트리

'''
크루스칼 - 자기 자신을 먼저 부모노드로 설정
집합 내에 가장 작은 수가 부모노드
부모가 동일한 애들끼리 합치면 사이클 형성 -> 빠꾸
V - 정점의 개수
E - 간선의 개수
'''
V, E = map(int,input().split())

node = [tuple(map(int, input().split())) for _ in range(E)]
node.sort(key=lambda x:x[2])
parent = [i for i in range(V+1)]
total_weight = 0
# 부모 찾기
if V ==1:
    print(0)
    exit()

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for A, B, cost in node:
    if find_parent(A) != find_parent(B):
        union(A, B)
        total_weight += cost

print(total_weight)