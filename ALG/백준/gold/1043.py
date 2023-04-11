# 구라

N, M = map(int, input().split())
trues = list(map(int,input().split()))
person = [[] for _ in range(N+1)]

if trues == [0]:
    print(M)
    exit()