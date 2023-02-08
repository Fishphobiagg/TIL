# 수 찾기

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()
B.sort()
for num in B:
    for num_a in A:
        print(num, num_a)
        if num_a == num:
            print(1)
            break
        elif num_a > num:
            print(0)
            break