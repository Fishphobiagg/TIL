T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A, B = list(map(int, input().split()))
    result = []
    if len(A) > len(B):
        for i in range(len(A)-len(B)):
            result = list(map(''))
a = 1