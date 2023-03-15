# 주사위

'''
모서리 개수 -
3면의 최대값을 구해야되는 개수 - 4개
2면의 최대값을 구해야되는 개수 - (N-1)*4개
1면의 최대값을 구해야되는 개수 - 5*(N**2) - 4*3 - (N-1)*4*2
'''
N = int(input())
if N == 1:
    dice = list(map(int,input().split()))
    print(sum(dice) - max(dice))
    exit()

dice = list(map(int, input().split()))
two_face = [dice[i]+dice[j] if i+j != 5 and i!=j else max(dice)*2+1 for i in range(6) for j in range(6)]
three_face = [dice[i]+dice[j]+dice[k] if i+k!=5 and i+j!=5 and k+j!=5 and i!=j and i!=k and j!=k else max(dice)*3+1 for i in range(6) for j in range(6) for k in range(6)]
one = ((N-2)**2)*5+(N-2)*4
two = (N-1)*4+(N-2)*4
three = 4
print(one*min(dice)+two*min(two_face)+three*min(three_face))
