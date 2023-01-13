x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

if (x_a-x_b)*(y_a-y_c) == (y_a-y_b)*(x_a-x_c):
    print(-1.0)
    exit(0)

a = ((x_a - x_b)**2 + (y_a - y_b)**2)**0.5
b = ((x_b - x_c)**2 + (y_b - y_c)**2)**0.5
c = ((x_c - x_a)**2 + (y_c - y_a)**2)**0.5

length = [a+c, a+b, c+b]
result = max(length) - min(length)

print(2*result)