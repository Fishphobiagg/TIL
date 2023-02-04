M, N = map(int, input().split())

sieve = [True] * (N+1)

m = int(N**0.5)

for i in range(2, m+1):
    if sieve[i] == True:
        j = 2
        while i*j <=N:
            sieve[i*j] = False
            j+=1
for i in range(M, N+1):
    if sieve[i]:
        if i != 1:
            print(i)
