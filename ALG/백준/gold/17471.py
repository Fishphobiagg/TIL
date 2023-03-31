# 리쌍


N = int(input())
population = list(map(int, input().split())) # 인구
node = [[] for _ in range(N+1)] # 각 간선 연결받기
for i in range(1, N+1):
    for a in list(map(int,input().split()))[1:]: # 간선 추가
        node[i].append(a)
ans = 1e7
population = [0] + population
all_set = [] # 두 개로 나눈 조합 저장할 리스트
def subset(x, left=[], right=[]):
    if x > N:
        if left and right:
            
            all_set.append((left, right))
            return
        return
    subset(x+1, left+[x], right)
    subset(x+1, left, right+[x])

def dfs(x, friend): # 나눠진 집합이 연결되어있는지 확인하기 위한 dfs
    global cnt
    for i in node[x]:
        if i in friend: # 만약 같은 집합?
            if not visited[i]: # 아직 노방문?
                visited[i] = 1
                cnt += 1
                dfs(i, friend)
# 두 집합으로 나누기
subset(1)
# 나뉜 집합이 가능한 집합인지 체크
for left, right in all_set:
    parent = list(range(N+1))
    cnt = 2
    visited = [0] * (N + 1)
    visited[min(left)] = 1
    dfs(left[0],left)
    visited = [0] * (N + 1)
    visited[min(right)] = 1
    dfs(right[0],right)
    if cnt == N:
        ans = min(ans, abs(sum([population[i] for i in left]) - sum([population[i] for i in right])))

if ans == 1e7:
    print(-1)
else:
    print(ans)