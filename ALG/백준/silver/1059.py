# 좋은 구간

N = int(input())
arr = list(map(int, input().split()))
target = int(input())

min = 0
max = 0
arr = sorted(arr)


for a in arr:
    if a < target:
        min = a
    elif a < target and max == 0:
        max = a

print((max-target)*(target-min)-1)