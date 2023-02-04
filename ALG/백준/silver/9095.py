N = int(input())
a = [1, 2, 4]
while len(a) < 10:
    a.append(a[len(a)-1]+a[len(a)-2]+a[len(a)-3])
for i in range(N):
    n = int(input())
    print(a[n-1])
    