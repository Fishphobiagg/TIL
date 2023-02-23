# 주사위 쌓기

'''
N =주사위의 개수
A B C D E F순서로 입력
A가 밑면일 경우 윗면 - F인덱스 상(0, 5) 1번째 세트
B가 밑면일 경우 윗면 - D (1, 3) 2번째 세트
C가 밑면일 경우 윗면 - E (2, 4) 3번째 세트
DEF는 그 역
가장 밑에 주사위의 가장 밑 면이 정해지는 순간 위 주사위들의 면은 정해진다.
즉 해당 문제에서 비교해야될 값은 가장 첫 주사위의 밑면 경우의 수인 6개만 있음.
'''

N = int(input())
# 주사위 셋 만들어주기
def other_side(x):
    if not x:
        return 5
    if x == 1:
        return 3
    if x == 3:
        return 1
    if x == 2:
        return 4
    if x == 4:
        return 2
    if x == 5:
        return 0


dice_set = [list(map(int, input().split())) for _ in range(N)]
max_result = 0
for i in range(6): # 처음 바닥 인덱스를 정하는 반복문, 경우의 수 6가지
    result = 0
    for j in range(N): # top은 꼭대기 인덱스, bottom은 바닥 인덱스
        dice = [k for k in range(1, 7)] # 1~6까지 주사위 눈
        if j == 0: # 0일 경우만 바닥면 i로 설정
            bottom = i
            top = other_side(bottom)
            dice.remove(dice_set[j][bottom])
            dice.remove(dice_set[j][top])
            result += max(dice)
        else:
            bottom = dice_set[j].index(dice_set[j-1][top]) # 바닥 인덱스 = 이전 주사위 꼭대기 값과 같은 같은 값을 가지는 면
            top = other_side(bottom) # 바닥 면의 반대편
            dice.remove(dice_set[j][top])
            dice.remove(dice_set[j][bottom])
            result += max(dice)
    if result > max_result:
        max_result = result
print(max_result)