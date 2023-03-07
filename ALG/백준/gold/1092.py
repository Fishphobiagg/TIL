# ship

'''
크레인의 무게 제한
M = 박스의 수
M개 박스의 무게 (최대 1만)

항상 그 크레인이 들 수 있는 최대값을 들어야 한다.(크레인은 오름차순으로 행동)
좌-우로 나누기?
퀵소트 피봇이 크레인이다.
'''

N = int(input())
crains = sorted(list(map(int, input().split())))
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if crains[-1] < boxes[0]:
    print(-1)
    exit()

time = 0
cant_move = 0
complete = 0

while complete < M:
    for i in range(N-1, cant_move-1, -1):
        if boxes[-1] > crains[i]:
            cant_move+=1
            continue
        for box in boxes:
            if box <= crains[i]:
                complete += 1
                boxes.remove(box)
                break
        if not boxes:
            break
    time += 1
print(time)