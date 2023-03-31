# 리쌍

'''
인접한 도시끼리 적절하게 나눠서 인구수차이를 최소화시킨다
'''

N = int(input())
population = list(map(int, input().split()))
node = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for a in list(map(int,input().split()))[1:]:
        node[i].append(a)
ans = 1e7
population = [0] + population
all_set = []
def subset(x, left=[], right=[]):
    if x > N:
        if left and right:
            all_set.append((left, right))
            return
        return
    subset(x+1, left+[x], right)
    subset(x+1, left, right+[x])

def dfs(x, friend):
    global cnt
    for i in node[x]:
        if i in friend:
            if not visited[i]:
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