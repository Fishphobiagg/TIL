# 3x + 5y

N = int(input())
cant_list = [1,2,4,7]
a = N // 5
b = (N - 5 * a) // 3
c = a*5 +b*3
while a*5 + b*3 !=N :
    if N in cant_list:
        print(-1)
        exit(0)
    if c < N:
        a -= 1
        b += 2
    else:
        a -= 1
        b += 1    

print(a+b)