N = int(input())
num = 1
count = 0

while num <= N:
    if len(str(num)) == 1 or len(str(num)) ==2:
        count += 1
        num += 1
    else:
        num_list = [j for j in str(num)]
        a = int(num_list[2]) - int(num_list[1])
        b = int(num_list[1]) - int(num_list[0])
        if (a >= 0 and b >= 0 and a == b) or (a <= 0 and b <= 0 and a == b):
            count += 1
            num += 1
        else:
            num += 1
print(count)
