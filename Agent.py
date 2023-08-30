class Agent:

    def calcularMovimientos(self, tablero):
        jugadas = []
        for row in range(9):
            for col in range(9):
                if (col <= 5):
                    if (tablero[row][col] == tablero[row][col+2] and tablero[row][col] == tablero[row][col+3]):
                        jugadas.append((col,row,'R'))
                if (col >= 3):
                    if (tablero[row][col] == tablero[row][col-2] and tablero[row][col] == tablero[row][col-3]):
                        jugadas.append((col,row,'L'))    
                if (row <= 5):
                    if (tablero[row][col] == tablero[row+2][col] and tablero[row][col] == tablero[row+3][col]):
                        jugadas.append((col,row,'D'))
                if (col >= 3):
                    if (tablero[row][col] == tablero[row-2][col] and tablero[row][col] == tablero[row-3][col]):
                        jugadas.append((col,row,'U'))                      
        return jugadas
    


##############
# Test Agnet #
##############

# myAgent = Agent()

# board = [
#     ['R', 'O', 'R', 'Y', 'B', 'R', 'P', 'O', 'Y'], 
#     ['O', 'B', 'Y', 'G', 'O', 'G', 'B', 'G', 'P'], 
#     ['G', 'G', 'B', 'O', 'G', 'O', 'R', 'P', 'O'], 
#     ['P', 'G', 'R', 'B', 'G', 'R', 'B', 'Y', 'P'], 
#     ['P', 'B', 'B', 'O', 'P', 'P', 'Y', 'Y', 'B'], 
#     ['O', 'O', 'B', 'P', 'R', 'P', 'R', 'B', 'O'], 
#     ['O', 'P', 'Y', 'R', 'R', 'B', 'O', 'O', 'Y'], 
#     ['P', 'P', 'Y', 'O', 'B', 'G', 'B', 'R', 'G'], 
#     ['O', 'O', 'P', 'O', 'G', 'Y', 'G', 'B', 'B']
#     ]


# print (myAgent.calcularMovimientos(board))