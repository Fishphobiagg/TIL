T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    a = 1
    b = 1
    for i in range(N):
        a *= M
        b *= N
        M -= 1
        N -= 1
    print(int(a/b))