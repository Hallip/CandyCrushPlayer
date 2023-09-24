class Agent:

    def calcularPuntaje(self, tablero, jugada):
        x, y, m =  jugada
        if m == 'U':
            tablero[y][x], tablero[y-1][x] = tablero[y-1][x], tablero[y][x]
        
        return tablero
    def calcularMovimientos(self, tablero):
        jugadas = []
        for row in range(9):
            for col in range(9):
                #   x . x x  
                if (col <= 5):
                    if (tablero[row][col] == tablero[row][col+2] and tablero[row][col] == tablero[row][col+3]):
                        jugadas.append((col,row,'R'))
                #   x . x x  
                if (col >= 3):
                    if (tablero[row][col] == tablero[row][col-2] and tablero[row][col] == tablero[row][col-3]):
                        jugadas.append((col,row,'L'))
                #   x . .  
                #   . x x
                if (col <= 6 and row <= 7):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row+1][col+2]):
                        jugadas.append((col,row,'D'))
                #   . x x  
                #   x . .
                if (col <= 6 and row >= 1):
                    if (tablero[row][col] == tablero[row-1][col+1] and tablero[row][col] == tablero[row-1][col+2]):
                        jugadas.append((col,row,'U'))
                #   . x .  
                #   x . x
                if (col <= 7 and row <= 7 and col >= 1):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row+1][col-1]):
                        jugadas.append((col,row,'D'))
                        print(tablero[row][col])
                #   x . x  
                #   . x .
                if (col <= 7 and col >= 1 and row >= 1):
                    if (tablero[row][col] == tablero[row-1][col+1] and tablero[row][col] == tablero[row-1][col-1]):
                        jugadas.append((col,row,'U'))
                        print(tablero[row][col])
                #   . . x  
                #   x x .
                if ( row <= 7 and col >= 2):
                    if (tablero[row][col] == tablero[row+1][col-1] and tablero[row][col] == tablero[row+1][col-2]):
                        jugadas.append((col,row,'D'))
                #   x x .  
                #   . . x
                if (col >= 2 and row >= 1):
                    if (tablero[row][col] == tablero[row-1][col-1] and tablero[row][col] == tablero[row-1][col-2]):
                        jugadas.append((col,row,'U'))
                #   x
                #   .
                #   x
                #   x
                if (row <= 5):
                    if (tablero[row][col] == tablero[row+2][col] and tablero[row][col] == tablero[row+3][col]):
                        jugadas.append((col,row,'D'))
                #   x
                #   x
                #   .
                #   x
                if (row >= 3):
                    if (tablero[row][col] == tablero[row-2][col] and tablero[row][col] == tablero[row-3][col]):
                        jugadas.append((col,row,'U'))
                #   . x
                #   x .
                #   x .
                if (col >= 1 and row <= 6):
                    if (tablero[row][col] == tablero[row+1][col-1] and tablero[row][col] == tablero[row+2][col-1]):
                        jugadas.append((col,row,'L'))
                #   x .
                #   . x
                #   . x
                if (col <= 7 and row <= 6):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row+2][col+1]):
                        jugadas.append((col,row,'R'))
                #   x .
                #   . x
                #   x .
                if (col >= 1 and row <= 7 and row >=1):
                    if (tablero[row][col] == tablero[row+1][col-1] and tablero[row][col] == tablero[row-1][col-1]):
                        jugadas.append((col,row,'L'))
                #   . x
                #   x .
                #   . x
                if (col <= 7 and row <= 7 and row >=1):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row-1][col+1]):
                        jugadas.append((col,row,'R'))
                #   x .
                #   x .
                #   . x
                if (col >= 1 and  row >=2):
                    if (tablero[row][col] == tablero[row-1][col-1] and tablero[row][col] == tablero[row-2][col-1]):
                        jugadas.append((col,row,'L'))
                #   . x
                #   . x
                #   x .
                if (col <= 7 and row >=2):
                    if (tablero[row][col] == tablero[row-1][col+1] and tablero[row][col] == tablero[row-2][col+1]):
                        jugadas.append((col,row,'R'))
        return jugadas[::-1]
    


##############
# Test Agnet #
##############

myAgent = Agent()

board = [
    ['R', 'O', 'R', 'Y', 'B', 'R', 'P', 'O', 'G'], 
    ['O', 'B', 'Y', 'G', 'O', 'G', 'B', 'G', 'G'], 
    ['G', 'G', 'B', 'O', 'G', 'O', 'O', 'P', 'O'], 
    ['P', 'G', 'R', 'B', 'O', 'R', 'B', 'Y', 'P'], 
    ['P', 'B', 'B', 'O', 'P', 'Y', 'P', 'Y', 'B'], 
    ['O', 'O', 'B', 'P', 'R', 'P', 'R', 'B', 'O'], 
    ['O', 'P', 'Y', 'R', 'R', 'B', 'O', 'O', 'Y'], 
    ['P', 'P', 'Y', 'O', 'B', 'G', 'B', 'R', 'G'], 
    ['O', 'O', 'P', 'O', 'G', 'Y', 'G', 'B', 'G']
    ]


print (myAgent.calcularMovimientos(board))

print(myAgent.calcularPuntaje(board, (2, 8, 'U')))