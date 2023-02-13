# 에디터

# 스택 양분

stack_1 = list(input())
stack_2 = []
cursor = len(stack_1)
N = int(input())

for i in range(N):
    command = input()
    if command == 'L' and stack_1:
        stack_2.append(stack_1.pop(stack_1[-1]))
    if command == 'D' and stack_2:
        stack_1.append(stack_2.pop(stack_2[-1]))
    if command == 'B' and stack_1:
        stack_1.pop(stack_1[-1])
    if command[0] == 'P':
        stack_1.append(command[-1])
print(*stack_1, sep='')