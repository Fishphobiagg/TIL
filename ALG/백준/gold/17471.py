# 리쌍

'''
인접한 도시끼리 적절하게 나눠서 인구수차이를 최소화시킨다
'''

N = int(input())
population = [0] + list(map(int, input().split()))
node = [[]for _ in range(N+1)]

for i in range(N):
    connect = list(map(int,input().split()))
    for j in range(1,len(connect)):
        node[i].append(connect[j])