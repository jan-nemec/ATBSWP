grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(grid[0][0])
# print(grid[1][0])
# print(grid[2][0])
# .
# .
# .
# print(grid[8][0])

# print(grid[0][1])
# print(grid[1][1])
# .
# .
# .
# print(grid[8][1])

numrows = len(input)    # 3 rows in your example
numcols = len(input[0])  # 2 columns in your example

for x in range(6):
    for y in range(9):
        print(grid[y][x], end='')
    print()
