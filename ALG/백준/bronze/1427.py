n = input()
a = []
b = ''
for i in n:
    a.append(int(i))
a = reversed(sorted(a))
for i in a:
    b += str(i)
print(b)