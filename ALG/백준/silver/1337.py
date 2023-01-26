# 올바른 배열
N = int(input())

arr = [int(input()) for i in range(N)]
result = 5
for a in arr:
    result_list = []
    check_list = [a + i for i in range(5)]
    for c in check_list:
        if c not in arr:
            result_list.append(c)
    if len(result_list) < result:
        result = len(result_list)
print(result)