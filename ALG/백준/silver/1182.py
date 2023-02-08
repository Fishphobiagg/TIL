# 부분수열의 합

N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
for i in range(1<<N):
    a = 0
    for j in range(N):
        if i & (1<<j):
            a += num[j]
    if i != 0 and a == S:
        cnt+=1
print(cnt)