N = int(input())
a = list(map(int, input().split()))

result = 0
for i in a:
    count = 0
    n = 1
    while n <= i:
        if i % n == 0:
            count += 1
            n += 1
        else:
            n += 1
    if count == 2:
        result +=1

print(result)