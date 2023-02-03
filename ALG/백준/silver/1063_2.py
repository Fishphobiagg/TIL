# 킹

stone, k, N = map(str, input().split())

moving_list = [input() for i in range(int(N))]

def alp_mapping(S, KING):
    S = S.translate(str.maketrans('ABCDEFGH', '12345678'))
    KING = KING.translate(str.maketrans('ABCDEFGH', '12345678'))
    return S, KING
def num_mapping(S, KING):
    S = S[0].translate(str.maketrans('12345678', 'ABCDEFGH')) + S[1]
    KING = KING[0].translate(str.maketrans('12345678', 'ABCDEFGH')) + KING[1]
    return S, KING       

stone, k = alp_mapping(stone, k)
stone_X, stone_Y, king_X, king_Y = map(int, [stone[0], stone[1], k[0], k[1]])

for moving in moving_list:
    if moving == 'R': 
        if stone_X != 8 and king_X != 8:
            stone_X +=1
            king_X +=1
        else:
            continue
    if moving == 'L': 
        if stone_X != 1 and king_X != 1:
            stone_X -=1
            king_X -=1
        else:
            continue
    if moving == 'T': 
        if stone_Y != 8 and king_Y != 8:
            stone_Y +=1
            king_Y +=1
        else:
            continue
    if moving == 'B':
        if stone_X != 1 and king_X != 1:
            stone_X -=1
            king_X -=1
        else:
            continue
    if moving == 'RT': 
        if stone_X != 8 and king_X != 8 and stone_Y !=8 and king_Y !=8:
            stone_X +=1
            king_X +=1
            stone_Y +=1
            king_Y +=1
        else:
            continue
    if moving == 'RB':
        if stone_X != 8 and king_X != 8 and stone_Y !=1 and king_Y !=1:
            stone_X+=1
            king_X+=1
            stone_Y-=1
            king_Y-=1
        else:
            continue    
    if moving == 'LT':
        if stone_X != 1 and king_X != 1 and stone_Y !=8 and king_Y !=8:
            stone_X -=1
            king_X -=1
            stone_Y +=1
            king_Y +=1
        else:
            continue
    if moving == 'LB':
        if stone_X != 1 and king_X != 1 and stone_Y !=1 and king_Y !=1:
            stone_X-=1
            king_X-=1
            stone_Y-=1
            king_Y -=1
        else:
            continue

stone_X, stone_Y, king_X, king_Y = map(str, [stone_X, stone_Y, king_X, king_Y])
for coordinate in num_mapping(stone_X+stone_Y, king_X+king_Y):
    print(coordinate)

