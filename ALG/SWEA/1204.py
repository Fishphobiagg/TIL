# 1204번 최빈수 구하기

T = int(input())

for i in range(T):
    a = []
    count = 0
    most_num = 0
    for _ in range(1000):
        b = int(input())
        a.append(b)
        if count < a.count(b):
            count = a.count(b)
            most_num = b
        elif count == a.count(b):
            if most_num < b:
                most_num = b
            else:
                continue
print(most_num)