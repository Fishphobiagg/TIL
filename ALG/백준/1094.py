#2진법
X = int(input())
count = 0
stick = [32, 16, 8, 4, 2, 1]

if X == 64:
    print(1)
    exit(0)
else:
    for i in stick:
        if X > i:
            X -= i
            count += 1
        elif X == i:
            print(count+1)
        else:
            continue