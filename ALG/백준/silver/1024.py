# 수열의 합

N, L = map(int,input().split())

for i in range(L, 100):
    a = N/i - i/2 + 1/2

    if int(a)-a == 0 and a >= 0:
        for j in range(int(a), int(a)+i):
            print(j, end=' ')
        exit()
print(-1)