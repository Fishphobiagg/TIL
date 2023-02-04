# 간단한 소인수분해

T = int(input())

for _ in range(T):
    num = int(input())
    counter = [0 for i in range(5)]
    number = [2, 3, 5, 7, 11]
    divide_idx = -1
    while num != 1:
        if num % number[divide_idx] == 0:
            num /= number[divide_idx]
            counter[divide_idx] += 1
        else:
            divide_idx -=1
    print(f'#{_+1} {counter[0]} {counter[1]} {counter[2]} {counter[3]} {counter[4]}')