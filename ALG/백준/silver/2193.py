n = int(input())
count_list = [1]

for i in range(0,n-1):
    count_list.append(sum(count_list[:i])+1)
    print(count_list)

print(max(count_list))