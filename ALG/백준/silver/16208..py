# 귀찮음

n = int(input())
stick = list(map (int,(input().split())))
a = sum(stick)
stick.sort()
total = 0
for i in stick:
    a-= i
    total += i*a
print(total)

'''
최소 or 최대값부터 잘라가면 된다.
'''