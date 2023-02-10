# 완전제곱수
import math
M = int(input())
N = int(input())
min_square_number = (int(math.sqrt(N))+1)**2
square_number = 0
for i in range(int(math.sqrt(M)), int(math.sqrt(N))+1):
    if M <= i**2 <= N:
        square_number+= i**2
        if i**2 < min_square_number:
            min_square_number = i**2
if square_number == 0:
    print(-1)
else:
    print(square_number)
    print(min_square_number)