import copy

class Agent:

    def simularJugada(self, tablero, jugada):
        x, y, m =  jugada
        newTab = []
        for row in tablero:
            myRow = []
            for col in row:
                myRow.append(col)
            newTab.append(myRow)
        if m == 'U':
            newTab[y][x], newTab[y-1][x] = newTab[y-1][x], newTab[y][x]
        elif m == 'D':
            newTab[y][x], newTab[y+1][x] = newTab[y+1][x], newTab[y][x]
        elif m == 'L':
            newTab[y][x], newTab[y][x-1] = newTab[y][x-1], newTab[y][x]
        elif m == 'R':
            newTab[y][x], newTab[y][x+1] = newTab[y][x+1], newTab[y][x]
        
        return newTab

    def calcularPuntaje(self, tablero):
        current_x = ''
        consecutive_x = 1
        current_y = ''
        consecutive_y = 1
        score = 0
        for row in range(9):
            if consecutive_y >= 3:
                        score = score + consecutive_y * 20
            if consecutive_x >= 3:
                        score = score + consecutive_x * 20            
            consecutive_x = 0
            consecutive_y = 0
            
            for col in range(9):
                if tablero[row][col] == current_x:
                    consecutive_x += 1
                else: 
                    if consecutive_x >= 3:
                        score = score + consecutive_x * 20
                    current_x = tablero[row][col]
                    consecutive_x = 1
                
                if tablero[col][row] == current_y:
                    consecutive_y += 1
                else: 
                    if consecutive_y >= 3:
                        score = score + consecutive_y * 20
                    current_y = tablero[col][row]
                    consecutive_y = 1
        return score

    def calcularMovimientos(self, tablero):
        jugadas = []
        for row in range(9):
            for col in range(9):
                #   x . x x  
                if (col <= 5):
                    if (tablero[row][col] == tablero[row][col+2] and tablero[row][col] == tablero[row][col+3]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'R'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'R',score,1))
                #   x . x x  
                if (col >= 3):
                    if (tablero[row][col] == tablero[row][col-2] and tablero[row][col] == tablero[row][col-3]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'L'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'L',score,2))
                #   x . .  
                #   . x x
                if (col <= 6 and row <= 7):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row+1][col+2]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'D'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'D',score,3))
                #   . x x  
                #   x . .
                if (col <= 6 and row >= 1):
                    if (tablero[row][col] == tablero[row-1][col+1] and tablero[row][col] == tablero[row-1][col+2]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'U'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'U',score,4))
                #   . x .  
                #   x . x
                if (col <= 7 and row <= 7 and col >= 1):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row+1][col-1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'D'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'D',score,5))
                #   x . x  
                #   . x .
                if (col <= 7 and col >= 1 and row >= 1):
                    if (tablero[row][col] == tablero[row-1][col+1] and tablero[row][col] == tablero[row-1][col-1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'U'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'U',score,6))
                #   . . x  
                #   x x .
                if ( row <= 7 and col >= 2):
                    if (tablero[row][col] == tablero[row+1][col-1] and tablero[row][col] == tablero[row+1][col-2]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'D'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'D',score,7))
                #   x x .  
                #   . . x
                if (col >= 2 and row >= 1):
                    if (tablero[row][col] == tablero[row-1][col-1] and tablero[row][col] == tablero[row-1][col-2]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'U'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'U',score,8))
                #   x
                #   .
                #   x
                #   x
                if (row <= 5):
                    if (tablero[row][col] == tablero[row+2][col] and tablero[row][col] == tablero[row+3][col]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'D'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'D',score,9))
                #   x
                #   x
                #   .
                #   x
                if (row >= 3):
                    if (tablero[row][col] == tablero[row-2][col] and tablero[row][col] == tablero[row-3][col]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'U'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'U',score,10))
                #   . x
                #   x .
                #   x .
                if (col >= 1 and row <= 6):
                    if (tablero[row][col] == tablero[row+1][col-1] and tablero[row][col] == tablero[row+2][col-1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'L'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'L',score,11))
                #   x .
                #   . x
                #   . x
                if (col <= 7 and row <= 6):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row+2][col+1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'R'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'R',score,12))
                #   x .
                #   . x
                #   x .
                if (col >= 1 and row <= 7 and row >=1):
                    if (tablero[row][col] == tablero[row+1][col-1] and tablero[row][col] == tablero[row-1][col-1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'L'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'L',score,13))
                #   . x
                #   x .
                #   . x
                if (col <= 7 and row <= 7 and row >=1):
                    if (tablero[row][col] == tablero[row+1][col+1] and tablero[row][col] == tablero[row-1][col+1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'R'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'R',score,14))
                #   x .
                #   x .
                #   . x
                if (col >= 1 and  row >=2):
                    if (tablero[row][col] == tablero[row-1][col-1] and tablero[row][col] == tablero[row-2][col-1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'L'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'L',score,15))
                #   . x
                #   . x
                #   x .
                if (col <= 7 and row >=2):
                    if (tablero[row][col] == tablero[row-1][col+1] and tablero[row][col] == tablero[row-2][col+1]):
                        tableroResultante = self.simularJugada(tablero, (col,row,'R'))
                        score = self.calcularPuntaje(tableroResultante)
                        jugadas.append((col,row,'R',score,16))
        # return jugadas[::-1]
        # print (jugadas)
        if (len(jugadas) < 1):
            return (1, 1, 'D', 0, 0)
        return max(jugadas[::-1], key=lambda x: x[3])


##############
# Test Agnet #
##############

# myAgent = Agent()

# board = [
#     ['O', 'B', 'O', (88, 110, 124), 'B', 'R', 'P', 'O', 'Y'], 
#     ['B', 'G', 'B', 'O', 'R', 'Y', 'G', 'G', 'R'], 
#     ['O', 'Y', 'R', 'R', 'G', 'P', 'B', 'G', 'P'], 
#     ['O', 'O', 'R', 'B', 'O', 'P', 'Y', 'O', 'R'], 
#     ['Y', 'B', 'G', 'P', 'G', 'O', 'P', 'P', 'O'], 
#     ['O', 'G', 'R', 'P', 'P', 'G', 'Y', 'Y', 'B'], 
#     ['R', 'B', 'Y', 'R', 'G', 'P', 'B', 'O', 'R'], 
#     ['Y', 'O', 'O', 'R', 'Y', 'O', 'B', 'Y', 'P'], 
#     ['P', 'O', 'P', 'R', 'G', 'Y', 'P', 'G', 'R']]


# print (myAgent.calcularMovimientos(board))

# # board = myAgent.simularJugada(board, (4, 8, 'L'))
# print("---------------------")
# print(myAgent.calcularPuntaje(board))