N = int(input())
dasom = int(input())
b = [int(input()) for i in range(N-1)]
dasom_first = dasom

b.sort(reverse=True)

if N == 1:
    print(0)
else:
    while b[0] >= dasom:
        dasom += 1
        b[0] -= 1
        b.sort(reverse=True)
    print(dasom-dasom_first)