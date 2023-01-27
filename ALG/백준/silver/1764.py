N, M = map(int, input().split())

s1 = set([input() for i in range(N)])
s2 = set([input() for i in range(M)])

print(len(s1&s2))
deudbojab = s1&s2
for name in sorted(deudbojab):
    print(name) 