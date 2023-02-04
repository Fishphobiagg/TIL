# 기차 사이의 파리

T = int(input())

for _ in range(T):
    D, A, B, F = map(int, input().split())

    print(f'#{_+1} {F*(D/(A+B))}')