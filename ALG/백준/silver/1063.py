# 킹

stone, k, N = map(str, input().split())

moving_list = [input() for i in range(int(N))]

def alp_mapping(S, KING):
    S = S.translate(str.maketrans('ABCDEFGH', '12345678'))
    KING = KING.translate(str.maketrans('ABCDEFGH', '12345678'))
    return S, KING
def num_mapping(S, KING):
    S = S.translate(str.maketrans('12345678', 'ABCDEFGH'))
    KING = KING.translate(str.maketrans('12345678', 'ABCDEFGH'))
    return S, KING       
def R(S, KING):
    alp_mapping(S, KING)
    if S[0] or KING[0] == '8':
        num_mapping(S, KING)
    else:
        S = str(int(S[0])+1) + S[1]
        KING = str(int(KING[0])+1) + KING[1]
        num_mapping(S, KING)
def L(S, KING):
    alp_mapping(S, KING)
    if S[0] or KING[0] == '1':
        num_mapping(S, KING)
    else:
        S = str(int(S[0])-1) + S[1]
        KING = str(int(KING[0])-1) + KING[1]
        num_mapping(S, KING)
def T(S, KING):
    alp_mapping(S, KING)
    if S[1] or KING[1] == '8':
        num_mapping(S, KING)
    else:
        S = str(int(S[1])+1) + S[0]
        KING = str(int(KING[1])+1) + KING[0]
        num_mapping(S, KING)
def B(S, KING):
    alp_mapping(S, KING)        
    if S[1] or KING[1] == '1':
        num_mapping(S, KING)
    else:
        S = str(int(S[1])-1) + S[0]
        KING = str(int(KING[1])-1) + KING[0]
        num_mapping(S, KING)
def RT(S, KING):
    alp_mapping(S, KING)
    if (S[0] or KING[0] == '8') or (S[1] or KING[1] == '8'):
        num_mapping(S, KING)
    else:
        R(S, KING)
        T(S, KING)
def LT(S, KING):
    alp_mapping(S, KING)
    if (S[0] or KING[0] == '1') or (S[1] or KING[1] == '8'):
        num_mapping(S, KING)
    else:
        L(S, KING)
        T(S, KING)
def RB(S, KING):
    alp_mapping(S, KING)   
    if (S[0] or KING[0] == '8') or (S[1] or KING[1] == '1'):
        num_mapping(S, KING)
    else:
        R(S, KING)
        B(S, KING)
def LB(S, KING):
    alp_mapping(S, KING)  
    if (S[0] or KING[0] == '1') or (S[1] or KING[1] == '1'):
        num_mapping(S, KING)
    else:
        L(S, KING)
        B(S, KING)

for moving in moving_list:
    if moving == 'R':
        R(stone, k)
    elif moving =='L':
        L(stone, k)
    elif moving =='T':
        T(stone, k)
    elif moving =='B':
        B(stone, k)
    elif moving =='RT':
        RT(stone, k)
    elif moving =='RB':
        RB(stone, k)
    elif moving =='LT':
        LT(stone, k)
    elif moving =='LB':
        LB(stone, k)

print(stone, k)