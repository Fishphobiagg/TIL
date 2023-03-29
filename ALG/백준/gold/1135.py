# 뉴스 전하기
'''
총 비용이 적은걸 선택 -> 재귀로 가장 밑까지 가야함
가장 밑에 있는 트리부터 최적의 값을 축적
갈림길에서 가장 노드의 비용이 큰 애들부터 선택
'''
N = int(input())
arr = list(map(int, input().split()))
tree = [[]for _ in range(N)]
for i in range(1,N):
    tree[arr[i]].append(i)

dp = [0]*(N)
def treedp(x):
    if tree[x]:
        under_tree = sorted([treedp(i) for i in tree[x]], reverse=True)
        dp[x] = max([i+1+under_tree[i] for i in range(0, len(tree[x]))])
    else:
        return dp[x]
    return dp[x]

treedp(0)
print(max(dp))
