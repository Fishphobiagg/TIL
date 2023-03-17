# 소트

'''
내 교환 횟수 내에서 범위가 닿는 최대 배열까지 가져오기
가져온 배열 내에서 최대값 맨 앞으로 당기기
최대값 index - 시작점 index만큼 교환횟수 차감
시작지점 + 1 
무한 반복
'''

N = int(input())
arr = list(map(int, input().split()))
chance = int(input())
start = 0

while chance and start < N - 1 and N > 1:
    bubble = arr[start:] if chance // (N - 1) else arr[start:start + chance + 1]
    chance -= arr.index(max(bubble)) - start
    bubble = [bubble.pop(bubble.index(max(bubble)))] + bubble
    for i in range(start, start + len(bubble)):
        arr[i] = bubble[i - start]
    start += 1

print(*arr)