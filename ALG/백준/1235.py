# 학생 번호
# 첫줄 다 같이 비교, 중복 안되는 애들 싹다 삭제?
N = int(input())

num_list = [input() for i in range(N)]
check_idx = 1

for j in range(len(num_list[0])):
    check_list = []
    for idx, num in enumerate(num_list):
        num = num[-check_idx:]
        if num not in check_list and idx+1 == len(num_list):
            print(check_idx)
            exit(0)
        elif num not in check_list:
            check_list.append(num)
        else:
            check_idx += 1