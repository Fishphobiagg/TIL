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
num_trunk = 0
def disjoint(x, y):
    if parent[x] == parent[y]: # 사이클 발생
        return False
    else:
        return True
start = min(node[0][0], node[0][1])
for A, B, weight in node:
    if parent[A] == parent[B]:
        continue
    if parent[A] == start or parent[B] == start:
        parent[A], parent[B] = start, start
    else:
        parent[A], parent[B] = min(parent[A], parent[B]), min(parent[A], parent[B])
    total_weight += weight
    num_trunk += 1
    if num_trunk == V-1:
        print(total_weight)
        break
