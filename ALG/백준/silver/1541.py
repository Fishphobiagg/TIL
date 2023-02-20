# 잃어버린 괄호

cul = input()
cul = list(cul.split('-'))
total = 0
if len(cul) == 1:
    if cul[0].isdigit():
        print(int(cul[0]))
        exit()
    else:
        total += sum(list(map(int, cul[0].split('+'))))
        print(total)
        exit()
if cul[0] == '':
    total -= sum(list(map(int, cul[1].split('+'))))
    for i in cul[2:]:
        total -= sum(list(map(int, i.split('+'))))
else:
    total += sum(list(map(int, cul[0].split('+'))))
    for i in cul[1:]:
        total -= sum(list(map(int, i.split('+'))))
print(total)
