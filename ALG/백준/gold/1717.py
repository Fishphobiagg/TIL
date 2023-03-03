# 집합의 표현
'''
트리를 이용한 집합의 표현
부모 노드를 설정해주고, 같은 부모노드를 갖고 있으면 YES
'''
N, M = map(int, input().split())

parents = [i for i in range(N+1)] # 부모를 자기 자신으로 설정

for i in range(M):
    command, a, b = map(int, input().split())
    if not command:
        parents[b] = parents[a]
    else:
        if parents[a] == parents[b]:
            print('yes')
        else:
            while parents[a] == parents[b]
            print('no')