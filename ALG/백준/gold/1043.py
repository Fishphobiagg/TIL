# 구라
'''
파티에 온 사람들은 모두 visited 처리
만약 다음 파티에 해당 사람들이 있을 경우 멈추고 떠들고 다닌 파티 말하기
'''
N, M = map(int, input().split())
trues = list(map(int,input().split()))[1:]
person = [[] for _ in range(N+1)]
party = [list(map(int,input().split()))[1:] for _ in range(M)]
if not trues:
    print(M)
    exit()

for k in party:
    for a in range(len(k)): # 기준 k, 붙일 애
        for j in range(len(k)):
            if j == a:
                continue
            person[k[a]].append(k[j])

def dfs(x):
    for i in person[x]:
        if i not in trues:
            trues.append(i)
            dfs(i)
first_true = trues[:]
for i in first_true:
    dfs(i)
ans = M
for i in party:
    for k in trues:
        if k in i:
            ans-=1
            break

print(ans)