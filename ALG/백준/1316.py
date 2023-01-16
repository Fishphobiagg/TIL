N = int(input())
count = N

for i in range(N):
    before = ''
    a = []
    b = input()
    for j in b:
        if j not in a or before == j:
            a.append(j)
        else:
            count -= 1
            break
        before = j

print(count)