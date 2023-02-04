room_num = [i for i in str(input())]
dict_count = {str(i) : 0 for i in range(0,10)}

for i in room_num:
    if i == '6' or i == '9':
        dict_count[i] += 0.5
    else:
        dict_count[i] += 1
dict_count['6 and 9'] = (dict_count['6']+dict_count['9'])
if type(dict_count['6 and 9']) == float:
    dict_count['6 and 9'] += 0.5

print(int(max(dict_count.values())))