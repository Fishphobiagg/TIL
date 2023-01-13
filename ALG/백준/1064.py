import math
x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

a = math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2)
b = math.sqrt((x_b - x_c)**2 + (y_b - y_c)**2)
c = math.sqrt((x_c - x_a)**2 + (y_c - y_a)**2)

if a == b:
    
elif b == c:
else:

A = [a, b, c]

print(A)