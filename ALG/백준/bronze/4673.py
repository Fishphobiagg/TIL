a = list(range(1, 10001))

remove_list=[]
for i in a:
    for num in str(i):
        i += int(num)
    if i > 10000:
        continue
    elif i not in remove_list:
        remove_list.append(i)
for i in remove_list:
    a.remove(i)
for i in a:
    print(i)
