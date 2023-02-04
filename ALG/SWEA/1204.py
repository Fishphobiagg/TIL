# 1204번 최빈수 구하기

T = int(input())

for _ in range(T):
    t = int(input())
    a = []
    count = 0
    most_num = 0
    b = list(map(int, input().split()))
    for j in b:
        a.append(j)
        if count < a.count(j):
            count = a.count(j)
            most_num = j
        elif count == a.count(j):
            if most_num < j:
                most_num = j
            else:
                pass
    print(f'#{t} {most_num}')