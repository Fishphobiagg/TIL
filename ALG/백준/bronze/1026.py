# 보물

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
C = sum([i * j for i, j in zip(A, B)])
print(C)