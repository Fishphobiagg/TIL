# 가르침
from itertools import combinations
'''
N = 입력받는 단어 개수
K = 사용하는 알파벳 개수

antic 개 알파벳 기본으로 가르쳐야함
가르칠수있는 알파벳의 개수는 정해져있다. 그렇기 떄문에 처음에 정하고,
그 알파벳을 배웠을때 읽을 수 있는 단어의 개수중 최대값을 출력하면 되는 문제
여집합의 부분집합을 구해서 최대한 많은 단어를 읽을 수 있을 경우 성공
'''


N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()

learned = ['a', 'n', 't', 'i', 'c']
unlearned = []
vocas = [input() for _ in range(N)]
learn_set = set(learned)
for voca in vocas:
    for i in (learn_set|set(list(voca))):
        if i not in learned:
            unlearned.append(i)
max_cnt = 0

if K == 5 or not unlearned:
    cnt = 0
    for voca in vocas:
        if len(learn_set|set(list(voca))) == 5:
            cnt+=1
    print(cnt)
    exit()

unlearned_set = set(unlearned)

for learnset in combinations(unlearned_set, K-5):
    cnt = 0
    for voca in vocas:
        if set(voca)|(set(learnset)|learn_set) == set(learnset)|learn_set:
            cnt+=1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)

