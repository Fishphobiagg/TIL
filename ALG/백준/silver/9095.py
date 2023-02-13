N = int(input())
a = [1, 2, 4]
while len(a) < 10:
    a.append(a[len(a)-1]+a[len(a)-2]+a[len(a)-3])
for i in range(N):
    n = int(input())
    print(a[n-1])

# 재귀함수

# 1, 2, 3 더하기

T = int(input())
num = [1, 2, 4]    
def plus(x):
    if x == 1 or x == 2 or x == 3:
        return num[x-1]
    else:
        return plus(x-1)+plus(x-2)+plus(x-3)

for test in range(T):
    print(plus(int(input())))