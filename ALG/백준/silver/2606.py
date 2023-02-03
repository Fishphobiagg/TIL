N = int(input())
connection = int(input())
infection = [[0*N]*N]

for i in range(connection):
    A, B = map(int, input().split())
    infection[A][B] = 1
    infection[B][A] = 1

print(infection)