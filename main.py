matrix=[['*','*','*'],
['*','*','*'],
['*','*','*']
        ]
ROWS=3
COLS=3
for i in range(ROWS):
   for j in range(COLS):
       print(matrix[i][j], end = " ")
   print()

win = False
while win == False:
    symbol = 'x'
    x = int(input())
    y = int(input())
    if (x>2 or x<0 or y>2 or y<0):
        print("ERROR UNPOSSIBLE X or Y")
        break
    matrix[x][y] = symbol
    symbol='o'
    for i in range(ROWS):
        for j in range(COLS):
            print(matrix[i][j], end=" ")
        print()
    x = int(input())
    y = int(input())
    if (x > 2 or x < 0 or y > 2 or y < 0):
        print("ERROR UNPOSSIBLE X or Y")
        break

    matrix[x][y] = symbol

    for i in range(ROWS):
        for j in range(COLS):
            print(matrix[i][j], end=" ")
        print()
    if (matrix[0][0]==matrix[0][1]==matrix[0][2]==symbol or
    matrix[1][0]==matrix[1][1]==matrix[1][2]==symbol or
    matrix[2][0]==matrix[2][1]==matrix[2][2]==symbol or
    matrix[0][0]==matrix[0][1]==matrix[0][2]==symbol or
    matrix[1][0]==matrix[1][1]==matrix[1][2]==symbol or
    matrix[2][0]==matrix[2][1]==matrix[2][2]==symbol or
    matrix[0][0]==matrix[1][1]==matrix[2][2]==symbol or
    matrix[2][0]==matrix[1][1]==matrix[0][2]==symbol):
        win = True
        print(symbol, 'win!')
        break
    else:
        continue

