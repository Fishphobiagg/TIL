stone, k, N = map(str, input().split())

moving_list = [input() for i in range(int(N))]

def alp_mapping(object):
    object = object.translate(str.maketrans('ABCDEFGH', '12345678'))
    return object
def num_mapping(object):
    object = object[0].translate(str.maketrans('12345678', 'ABCDEFGH')) + object[1]
    return object

def move(object,S, move_list):
    object = alp_mapping(object)
    object_X = int(object[0])
    object_Y = int(object[1])
    S = alp_mapping(object)
    
    def R(object_X):
        if object_X == 8:
            return object_X
        else:
            object_X +=1
            return object_X
    def L(object_X):
        if object_X == 1:
            return object_X
        else:
            object_X -=1
            return object_X
    def T(object_Y):
        if object_Y == 8:
            return object_Y
        else:
            object_Y +=1
            return object_Y
    def B(object_Y):
        if object_Y == 1:
            return object_Y
        else:
            object_Y -=1
            return object_Y
    def RT(object_X, object_Y):
        if object_X == 8 or object_Y == 8:
            return object_X, object_Y
        else:
            object_X +=1
            object_Y +=1
            return object_X, object_Y
    def RB(object_X, object_Y):
        if object_X == 8 or object_Y == 1:
            return object_X, object_Y
        else:
            object_X +=1
            object_Y -=1
            return object_X, object_Y
    def LT(object_X, object_Y):
        if object_X == 1 or object_Y == 8:
            return object_X, object_Y
        else:
            object_X -=1
            object_Y +=1
            return object_X, object_Y
    def LB(object_X, object_Y):
        if object_X == 1 or object_Y == 1:
            return object_X, object_Y
        else:
            object_X -=1
            object_Y -=1
            return object_X, object_Y
    for moving in move_list:
        if moving == 'R':
            object_X = R(object_X)
        elif moving == 'L':
            object_X = L(object_X)  
        elif moving == 'T':
            object_Y = T(object_Y)
        elif moving == 'B':
            object_Y = B(object_Y)
        elif moving == 'RT':
            object_X, object_Y = RT(object_X, object_Y)
        elif moving == 'LT':
            object_X, object_Y = LT(object_X, object_Y)
        elif moving == 'RB':
            object_X, object_Y = RB(object_X, object_Y)
        elif moving == 'LB':
            object_X, object_Y = LB(object_X, object_Y)
        print(object_X, object_Y)
    result = num_mapping(str(object_X)+str(object_Y))
    return result
print(move(k, moving_list), move(k, moving_list))
