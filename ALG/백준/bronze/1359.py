# 확률 문제네 조합 / 조합

N,M,K = map(int, input().split())

# 전체 경우의 수 구하기
denominator = 1
_N = N
factorial = 1
for i in range(1, M+1):
    denominator *= _N
    _N -= 1
    factorial *= i
denominator = denominator/factorial
print(denominator)

if M - (N-M) >= K:
    print(1.0)
else:
    while N > 1:
        break