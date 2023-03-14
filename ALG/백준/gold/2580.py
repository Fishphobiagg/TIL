sudoku = [list(map(int, input().split())) for _ in range(9)]
need = []

row = [[] for _ in range(9)]
box = [[] for _ in range(9)]
for i in range(9):
    for j in range(9):
        row[j].append(sudoku[j][i])
        box[(i//3)*3+j//3].append(sudoku[i][j])
        if not sudoku[i][j]:
            need.append((i,j))
def pos(x, i):
    if i not in sudoku[need[x][0]]:
        print(1)
    elif i not in sudoku[need[x][1]]:
        print(2)
    if i in sudoku[need[x][0]] or i in row[need[x][1]] or i in box[(need[x][0]//3)*3+need[x][0]//3]: # 가로 세로줄 검사
        return False
    else:
        return True
def backtracking(x):
    if x == len(need):
        for sudo in sudoku:
            print(*sudo)
        exit()
    else:
        for i in range(1, 10):
            sudoku[need[x][0]][need[x][1]] = i
            if sudoku[need[x][0]].count(i) <= 1 and row[need[x][1]].count(i) <= 1 and box[(need[x][0]//3)*3+need[x][0]//3].count(i) <= 1:
                backtracking(x+1)
backtracking(0)
print(sudoku)