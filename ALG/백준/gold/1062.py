# 가르침

'''
anta tica
# 기본 단어 a c i n t 
'''

basic = list('acint')
X_list = list('bdefghjklmopqrsuvwxyz')

N, M = map(int, input().split())
word_list = [input() for i in range(N)]
if M < 5:
    print(0)
book = []
def learn(x=0, words=list('acint')):
    if len(words)==M:
        book.append(words)
        return
    if x==len(X_list):
        return
    learn(x+1, words+X_list[x])
    learn(x+1, words)

res = 0

for i in book:
    ans = 0
    can_read = True
    for j in word_list:
        for k in j:
            if not k in i:
                can_read = False
                break
        ans + 1 if can_read else ans + 0
    ans = max(ans, res)